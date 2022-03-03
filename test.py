import requests

r = requests.post('https://courage-fraud-detection.herokuapp.com/is-fraud', json = {
        "step":1,
        "type":"PAYMENT",
        "amount":9839.64,
        "nameOrig":"C1231006815",
        "oldbalanceOrig":170136.0,
        "newbalanceOrig":160296.36,
        "nameDest":"M1979787155",
        "oldbalanceDest":0.0,
        "newbalanceDest":0.0
    })

print(r.text)