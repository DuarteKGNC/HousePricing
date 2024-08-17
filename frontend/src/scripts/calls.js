import axios from "axios";

const ENDPOINT = "http://127.0.0.1:8000/predict/" 

export async function make_prediction(data){
    const response = await axios.post(ENDPOINT, {'data': data})
    const value = Math.round(response.data.data[0][0]);
    if(value < 0){
        return 0;
    }
    return value;
}