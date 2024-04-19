<template>
    <div class="coffee-bean-form">
        <h2>咖啡豆資訊表單</h2>
        <form @submit.prevent="handleSubmit">
            <div>
                <label for="name">{{ formLabels.name }}</label>
                <input id="name" v-model="coffeeBean.name" type="text" required>
            </div>
            <div>
                <label for="roast_date">{{ formLabels.roastDate }}</label>
                <input id="roast_date" v-model="coffeeBean.roast_date" type="date" required>
            </div>
            <div>
                <label for="roast_level">{{ formLabels.roastLevel }}</label>
                <select id="roast_level" v-model="coffeeBean.roast_level" required>
                    <option v-for="option in roastLevelOptions" :key="option.value" :value="option.text">{{ option.text }}</option>
                </select>
            </div>
            <div>
                <label for="weight">{{ formLabels.weight }}</label>
                <input id="weight" v-model="coffeeBean.weight" type="number" @blur="validateQuantity" :class="{'input-error': errors.weight}" required>
                <div v-if="errors.weight" class="form-error">{{ errors.weight }}</div>
            </div>
            <div>
                <label for="origin">{{ formLabels.origin }}</label>
                <input id="origin" v-model="coffeeBean.origin" type="text">
            </div>
            <div>
                <label for="notes">{{ formLabels.notes }}</label>
                <textarea id="notes" v-model="coffeeBean.notes"></textarea>
            </div>
            <button type="submit">{{ formLabels.submitButton }}</button>
            <div v-if="formError" class="error">{{ formError }}</div>
            <div class="success-message">{{ successMessage }}</div>
        </form>
    </div>
</template>

<script>
    import { reactive, toRefs, ref, computed } from 'vue';
    import axios from 'axios';
    import zh from '@/i18n/locales/zh';
    import { useCoffeeBeansState } from './useCoffeeBeansState';

    export default {
        setup() {
            const coffeeBean = reactive({
                name: '',
                roast_date: '',
                roast_level: '',
                weight: '',
                origin: '',
                notes: '',
            });

            const successMessage = ref('');
            const errors = ref({});

            const formLabels = zh.formLabels

            const roastLevelOptions = computed(() => Object.entries(formLabels.roastLevelOptions).map(([value, text]) => ({ value, text })));

            const handleSubmit = async () => {
                if (!validateForm()) {
                    return;
                }

                try {
                    await axios.post('/api/coffeebeans/', coffeeBean);
                    successMessage.value = '咖啡豆資料新增成功';
                    resetForm();   
                    await useCoffeeBeansState().fetchCoffeeBeans(); // 從useCoffeeBeans中調用更新列表的方法
                } catch (error) {
                    console.error("新增咖啡豆失敗:", error);
                    successMessage.value = '新增咖啡豆失敗';
                }
            };

            const validateForm = () => {
                let isValid = true;
                errors.value = {};

                if (coffeeBean.weight < 0 ) {
                    errors.value.weight = '重量必須為正數。';
                    isValid = false;
                }

                return isValid;
            }

            const validateQuantity = () => {
                if (coffeeBean.weight < 0 ) {
                    errors.value.weight = '重量必須為正數。';
                } else {
                    errors.value.weight = '';
                }
            }

            const resetForm = () => {
                coffeeBean.name = '';
                coffeeBean.roast_date =  '';
                coffeeBean.roast_level = '';
                coffeeBean.weight = '';
                coffeeBean.origin = '';
                coffeeBean.notes = '';
                errors.value = {};

                setTimeout(() => {
                    successMessage.value = '';
                }, 3000)
            };


            return { 
                ...toRefs({coffeeBean}), 
                handleSubmit, 
                successMessage,
                errors,
                validateQuantity,
                formLabels,
                roastLevelOptions,
            };
        },
    }
</script>

<style>
    .coffee-bean-form {
        flex: 1;
        padding: 20px;
        margin: 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.1), inset 10px 10px 15px rgba(255, 255, 255, 0.05);

    }
    .success-message {
        color: green;
    }

    .form-error {
        color: #dc3545;
        margin-top: .25rem;
        font-size: .875em;
    }

    .input-error {
        border-color: #dc3545;
    }
</style>