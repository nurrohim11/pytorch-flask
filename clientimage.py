import requests

resp = requests.post("http://localhost:5000/predict",
    files={"file":open('E://kuliah//pyTorch//kucing.jpg','rb')})
    
print(resp.json())