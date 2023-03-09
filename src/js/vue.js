const app = Vue.createApp({
    data() {
        return {
            enteredQuery: '',
            isHidden: true,
            city: '',
            temp: '',
            icon: '',
            text: '',
            max: '',
            min: ''
        };
    },
    methods: {
        makeWeatherDisplay(data) {
            console.log(data);
            this.isHidden = false;
            this.city = data.city;
            this.temp = data.temp;
            this.icon = data.icon;
            this.text = data.text;
            this.max = data.maxtemp;
            this.min = data.mintemp;
        },
        fetchWeatherApi(data) {
            if (!this.enteredQuery) {
                this.isHidden = true;
                return;
            }
            $.post("/weather/js/api",
                {
                    q: this.enteredQuery,
                },
                (data, status) => {
                    this.makeWeatherDisplay(data);
                }
            ).fail((data, status) => {
                console.log(data.responseJSON["error"]);
                this.isHidden = true;
                alert(data.responseJSON["error"]);
            });
        }
    }
});

app.mount('#weather-display');