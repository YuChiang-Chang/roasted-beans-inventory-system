<template>
    <CoffeeBeanForm></CoffeeBeanForm>
    <CoffeeBeansList></CoffeeBeansList>
    <div>
    </div>
</template>

<script>
    import CoffeeBeanForm from '../components/CoffeeBeanForm.vue';
    import CoffeeBeansList from '../components/CoffeeBeansList.vue';

    export default {
        components: {
            CoffeeBeanForm,
            CoffeeBeansList,
        }
    }
</script>