import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',
      operadoras: [],
      isLoading: false,
      searchPerformed: false, 
      searchType: 'nome' 
    };
  },

  computed: {
    getPlaceholder() {
      switch (this.searchType) {
        case 'nome':
          return 'Digite o nome da operadora';
        case 'registro':
          return 'Digite o número do Registro ANS';
        case 'cnpj':
          return 'Digite o número do CNPJ';
        case 'modalidade':
          return 'Digite a modalidade da operadora';
        default:
          return 'Digite o termo de busca';
      }
    }
  },

  methods: {
    async buscarOperadoras(searchTerm, searchType) {
      if (searchTerm.trim() === '') {
        this.operadoras = [];
        return;
      }

      this.isLoading = true;
      let apiUrl = '';

      switch (searchType) {
        case 'nome':
          apiUrl = `http://127.0.0.1:5000/operadoras/busca?termo=${encodeURIComponent(searchTerm)}`;
          break;
        case 'registro':
          apiUrl = `http://127.0.0.1:5000/operadoras/registro?registro=${encodeURIComponent(searchTerm)}`;
          break;
        case 'cnpj':
          apiUrl = `http://127.0.0.1:5000/operadoras/cnpj?cnpj=${encodeURIComponent(searchTerm)}`;
          break;
        case 'modalidade':
          apiUrl = `http://127.0.0.1:5000/operadoras/modalidade?modalidade=${encodeURIComponent(searchTerm)}`;
          break;
        default:
          apiUrl = `http://127.0.0.1:5000/operadoras/busca?termo=${encodeURIComponent(searchTerm)}`;
      }

      try {
        const response = await axios.get(apiUrl);
        this.operadoras = response.data;
        console.log('Dados recebidos:', this.operadoras);
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
        this.operadoras = [];
      } finally {
        this.isLoading = false;
      }
    },
    async performSearch() {
      this.operadoras = [];
      this.isLoading = true;

      const searchTerm = this.searchQuery.trim();
      if (searchTerm === '') {
        this.isLoading = false;
        this.operadoras = [];
        return;
      }

      await this.buscarOperadoras(searchTerm, this.searchType);
      this.searchPerformed = true;
    }
  },
  mounted() {
    console.log('Componente carregado!');
  }
};