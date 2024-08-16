<template>
    <div class="housepricing">
        <h1 class="text-center">House Pricing Predictions</h1>
        <div class="d-flex flex-column gap-1 justify-content-center align-items-center mt-5">
            <div class="w-25">
                <InputField  v-for="(label, key) in input_labels" :key="key" :id="label.name" :placeholder="label.placeholder" v-on:changeValue="updateValues" />
                <div class="mt-3"></div>
                <ChoiceField v-for="(label, key) in multiple_choice_labels" :key="key" :label="label.name" :options="label.options" v-on:changeValue="updateValues" />
                <h3>Price: {{ price }}$</h3>
                <button class="btn btn-primary w-100 mt-2">Calculate Price</button>
            </div>
        </div>
    </div>
</template>
<script>
import InputField from './InputField.vue';
import ChoiceField from './ChoiceField.vue';
export default {
    name: 'HousePricing',
    components: {
        InputField,
        ChoiceField
    },
    data(){
        return{
            price: 0,
            input_labels: [
                    {name: 'area', placeholder: 'Area of the house in m2', value: 0},
                    {name: 'bedrooms', placeholder: 'Number of bedrooms', value: 0},
                    {name: 'bathrooms', placeholder: 'Number of bathrooms', value: 0},
                    {name: 'stories', placeholder: 'Number of stories', value: 0},
                    {name: 'guestrooms', placeholder: 'Number of guestrooms', value: 0},
            ],
            multiple_choice_labels: [
                    {name: 'Mainroad', options: ['Yes', 'No'], value: false},
                    {name: 'Basement', options: ['Yes', 'No'], value: false},
                    {name: 'Hot water', options: ['Yes', 'No'], value: false},
                    {name: 'Air Conditioning', options: ['Yes', 'No'], value: false},
                    {name: 'Parking', options: ['Yes', 'No'], value: false},
                    {name: 'Preferable Area', options: ['Yes', 'No'], value: false},
                    {name: 'Furnishing Dtatus', options: ['furnished', 'semi-furnished', 'unfurnished'], value: 'unfurnished'},
            ],
        }
    },
    methods: {
        updateValues(name, value, type){
            if(type === "single_input"){
                const object = this.input_labels.find(label => label.name === name);
                object.value = value;
            }else{
                const object = this.multiple_choice_labels.find(label => label.name === name);
                object.value = object.options[value];
            }
        }
    }
}
</script>