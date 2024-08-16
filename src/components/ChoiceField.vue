<template>
    <select class="form-select w-25">
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
    }
}
</script>