<template>
    <div>
        <div v-if="showMessage" class="message">{{ message }}</div>
        <h2>咖啡豆列表</h2>
        <ul>
            <li v-for="coffeeBean in coffeeBeans" :key="coffeeBean.id">
                名稱： {{ coffeeBean.name }}, 烘焙日期： {{ coffeeBean.roast_date }}, 烘焙程度： {{ coffeeBean.roast_level }}, {{ formLabels.weight }} {{ coffeeBean.weight }}, 產地： {{ coffeeBean.origin }}, 備註： {{coffeeBean.notes}}
                <button @click="editCoffeeBean(coffeeBean)">修改</button>
                <button @click="deleteCoffeeBean(coffeeBean.id)">刪除</button>
            </li>
        </ul>
        <EditCoffeeBeanDialog 
            v-if="isEditDialogVisible" 
            :coffeeBean="editableCoffeeBean" 
            :isVisible="isEditDialogVisible" 
            @update:isVisible="isEditDialogVisible = $event" 
            @save="handleSave">
        </EditCoffeeBeanDialog>
    </div>
</template>

<script>
    import { onMounted, ref, toRefs } from 'vue';
    import axios from 'axios';
    import { useMessageState } from './useMessageState';
    import { useCoffeeBeansState } from './useCoffeeBeansState';
    import EditCoffeeBeanDialog from './EditCoffeeBeanDialog.vue';
    import { formLabels } from '@/assets/formLabel';
    // import { useFetchCoffeeBeans } from './useFetchCoffeeBeans';
    // import  state  from './state';

    export default {
        components: {
            EditCoffeeBeanDialog
        },

        setup() {
            // const { error, fetchCoffeeBeans, isLoading } = useFetchCoffeeBeans();
            const { coffeeBeansState, fetchCoffeeBeans } = useCoffeeBeansState();
            const { coffeeBeans } = toRefs(coffeeBeansState);
            const { messageState, setMessage } = useMessageState();
            const isEditDialogVisible = ref(false);
            const editableCoffeeBean = ref({});

            onMounted(() => {
                useCoffeeBeansState().fetchCoffeeBeans();
            });

            const editCoffeeBean = (coffeeBean) => {
                    console.log('編輯咖啡豆', coffeeBean);
                    editableCoffeeBean.value = { ...coffeeBean };
                    // console.log('編輯咖啡豆', editableCoffeeBean);
                    isEditDialogVisible.value = true;
            };

            const deleteCoffeeBean = async (id) => {
                try {
                    await axios.delete(`http://localhost:8000/api/coffeebeans/${id}`)
                    setMessage('咖啡豆資料已刪除')
                    // alert('');
                    await fetchCoffeeBeans();
                } catch (error) {
                    console.error("刪除咖啡豆失敗：", error);
                    setMessage('刪除咖啡豆失敗')
                    // alert('');
                }
            };

            const handleSave = async (editedCoffeeBean) => {
                try {
                    await axios.put(`http://localhost:8000/api/coffeebeans/${editedCoffeeBean.id}/`, editedCoffeeBean);
                    await fetchCoffeeBeans();
                    setMessage('咖啡豆資料更新成功');
                    isEditDialogVisible.value = false;
                } catch (error) {
                    console.error("咖啡豆資料更新失敗：", error);
                    setMessage('咖啡豆資料更新失敗');
                    alert('咖啡豆資料更新失敗');
                }
            };


            return { 
                coffeeBeans, 
                editCoffeeBean, 
                deleteCoffeeBean, 
                message: messageState.message,
                showMessage: messageState.showMessage,
                isEditDialogVisible,
                editableCoffeeBean,
                handleSave,
                formLabels,
            };
        }
    }
</script>