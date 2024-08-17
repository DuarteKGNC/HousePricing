import axios from "axios";

const ENDPOINT = "http://127.0.0.1:8000/predict/" 

export function make_prediction(data){
    axios.post(ENDPOINT, {'data': data})
    .then(response => {
        return response.data.data[0][0];
    })
}