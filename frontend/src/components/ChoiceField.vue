<template>
    <select class="form-select mb-2" v-model="value">
        <option selected>{{$props.label}}</option>
        <option v-for="(option, index) in $props.options" :key="index" :value="index">{{option}}</option>
    </select>
</template>
<script>
export default {
    name: 'ChoiceField',
    props: {
        label: String,
        options: Array
    },
    data(){
        return {
            value: this.label
        }
    },
    watch:{
        value(e){
            if(typeof e === typeof 1){
                this.$emit("changeValue", this.label, this.value, 'multiple_input');
            }else{
                return false;
            }
        }
    }
}
</script>