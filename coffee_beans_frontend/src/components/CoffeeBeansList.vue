<template>
    <div class="coffee-beans-list">
        <div v-if="showMessage" class="message">{{ message }}</div>
        <h2>咖啡豆列表</h2>
        <ul>
            <li class="coffee-bean-item" v-for="coffeeBean in coffeeBeans" :key="coffeeBean.id">
                <div class="coffee-bean-property">
                    <span class="property-label">{{ formLabels.name }}</span>
                    <span class="property-value">{{ coffeeBean.name }}</span>
                </div>
                <div>
                    <span>{{ formLabels.roastDate }}</span>
                    <span>{{ coffeeBean.roast_date }}</span>
                </div>
                <div>
                    <span>{{ formLabels.roastLevel }}</span>
                    <span>{{ coffeeBean.roast_level }}</span>
                </div>
                <div>
                    <span>{{ formLabels.weight }}</span>
                    <span>{{ coffeeBean.weight }} 公克</span>
                </div>
                <div>
                    <span>{{ formLabels.origin }}</span>
                    <span>{{ coffeeBean.origin }}</span>
                </div>
                <div>
                    <span>{{ formLabels.notes }}</span>
                    <span>{{ coffeeBean.notes }}</span>
                </div>
                <div class="coffee-bean-actions">
                    <button @click="editCoffeeBean(coffeeBean)">{{ formLabels.editButton }}</button>
                    <button @click="deleteCoffeeBean(coffeeBean.id)">{{ formLabels.deleteButton }}</button>
                    <button @click="sellCoffeeBean(coffeeBean)">{{ formLabels.sellButton }}</button>
                </div>
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
    import zh from '@/i18n/locales/zh';
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
            const formLabels = zh.formLabels

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
                    await axios.delete(`/api/coffeebeans/${id}`)
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
                    await axios.put(`/api/coffeebeans/${editedCoffeeBean.id}/`, editedCoffeeBean);
                    await fetchCoffeeBeans();
                    setMessage('咖啡豆資料更新成功');
                    isEditDialogVisible.value = false;
                } catch (error) {
                    console.error("咖啡豆資料更新失敗：", error);
                    setMessage('咖啡豆資料更新失敗');
                    alert('咖啡豆資料更新失敗');
                }
            };

            const sellCoffeeBean = async (coffeeBean) => {
                // 使用 prompt 對話框讓用戶輸入賣出的重量
                const sellWeightStr = prompt('請輸入賣出的重量(公克)：', '454');

                if (sellWeightStr === null || sellWeightStr.trim() === '') {
                    return;
                }

                const sellWeight = parseInt(sellWeightStr, 10);

                // 檢查用戶輸入是否有效
                if (isNaN(sellWeight) || sellWeight <=0) {
                    alert('請輸入有效的重量！');
                    return;
                }

                try{
                    // 確保不會賣出超過當前重量的咖啡豆
                    const newWeight = Math.max(coffeeBean.weight - sellWeight, 0);

                    await axios.put(`/api/coffeebeans/${coffeeBean.id}/`, {
                        ...coffeeBean,
                        weight: newWeight
                    });
                    coffeeBean.weight = newWeight;
                } catch (error) {
                    console.error('賣出咖啡豆失敗', error);

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
                sellCoffeeBean,
            };
        }
    }
</script>

<style lang="scss">
    .coffee-beans-list {
        flex: 1;
        display: flex;
        /* flex-wrap: wrap; */
        flex-direction: column;
        margin: 20px;
        padding: 10px;
        // overflow:hidden;
        // overflow-y: scroll;
        background: rgba(255, 255, 255, 0.1);
        // backdrop-filter: blur(5px);
        border-radius: 15px;
        box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.1), inset 10px 10px 15px rgba(255, 255, 255, 0.05);
    }
    .coffee-beans-list ul{
        /* margin: 0; */
        padding: 0;
        list-style-type: none;
        display: flex;
        flex-direction: column;
        height: 100%;
        // overflow: hidden;
        // overflow-y: scroll;

        li {
            transition: 0.3s;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px;
            border-radius: 15px;
            backdrop-filter: blur(5px);
            background: rgba(255, 255, 255, 0.1);
            min-width: 20rem;

            &:hover {
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
        }
    }
</style>