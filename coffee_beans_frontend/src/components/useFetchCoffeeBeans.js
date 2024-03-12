// import { ref } from "vue";
// import axios from "axios";

// export function useFetchCoffeeBeans() {
//     const coffeeBeans = ref([]);
//     const isLoading = ref(false);
//     const error = ref(null);

//     const fetchCoffeeBeans = async () => {
//         isLoading.value = true;
//         error.value = null;
//         try {
//             const response = await axios.get('/api/coffeebeans/');
//             coffeeBeans.value = response.data;
//         } catch (err) {
//             error.value = err;
//             console.error("Fetching coffee beans failed:", err);
//         } finally {
//             isLoading.value = false;
//         }
//     }

//     return { coffeeBeans, isLoading, error, fetchCoffeeBeans };
// }
