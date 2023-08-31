const getCustomers = () => (
    {
        items: [],

        init(){
            this.getData()
        },

        getData() {
            const url = 'http://localhost:8000/api/v1/customer/customer'
            axios(url).then(response => this.items = response.data)
        },
    }
) 