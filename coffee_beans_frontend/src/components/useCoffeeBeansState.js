import { reactive, toRefs } from "vue";
import axios from "axios";

const state = reactive({
    coffeeBeans: [],
    isLoading: false,
    error: null,
});

async function fetchCoffeeBeans() {
    state.isLoading = true;
    state.error = null;
    try {
        const response = await axios.get('/api/coffeebeans/');
        state.coffeeBeans = response.data;
    } catch (error) {
        console.error("Fetching coffee beans failed:", error);
    } finally {
        state.isLoading = false
    }
}

export function useCoffeeBeansState () {
    return {
        coffeeBeansState: toRefs(state),
        fetchCoffeeBeans,
    }
}