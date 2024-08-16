<template>
    <div class="housepricing">
        <h1 class="text-center">House Pricing Predictions</h1>
        <div class="d-flex flex-column gap-1 justify-content-center align-items-center">
            <InputField  v-for="(label, key) in input_labels" :key="key" :id="label.name" :placeholder="label.placeholder" />
            <ChoiceField v-for="(label, key) in multiple_choice_labels" :key="key" :label="label.name" :options="label.options"/>
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
            input_labels: [
                    {name: 'area', value: undefined, placeholder: 'Area of the house in m2'},
                    {name: 'bedrooms', value: undefined, placeholder: 'Number of bedrooms'},
                    {name: 'bathrooms', value: undefined, placeholder: 'Number of bathrooms'},
                    {name: 'stories', value: undefined, placeholder: 'Number of stories'},
                    {name: 'guestrooms', value: undefined, placeholder: 'Number of guestrooms'},
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
    }
}
</script>