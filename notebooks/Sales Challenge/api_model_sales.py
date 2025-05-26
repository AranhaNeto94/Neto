from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Instância FastAPI
app = FastAPI()

# Classe de entrada
class RequestBody(BaseModel):
    tempo_de_experiencia: float
    numero_de_vendas: int
    fator_sazonal: int  # Agora esperamos um inteiro (não mais string)

# Carregar modelo e encoder
modelo_poly = joblib.load('./model_sales.pkl')
encoder_sazonal = joblib.load('./encoder_fator_sazonal.pkl')

@app.post('/predict')
def predict(data: RequestBody):
    try:
        # Codificar fator_sazonal
        fator_sazonal_encoded = encoder_sazonal.transform([data.fator_sazonal])[0]
    except ValueError:
        return {"erro": "Valor de fator_sazonal inválido. Deve ser um dos: " + str(list(encoder_sazonal.classes_))}

    # Criar DataFrame para predição
    input_data = {
        'tempo_de_experiencia': data.tempo_de_experiencia,
        'numero_de_vendas': data.numero_de_vendas,
        'fator_sazonal': fator_sazonal_encoded
    }

    df_input = pd.DataFrame([input_data])

    # Predizer
    y_pred = modelo_poly.predict(df_input)[0]

    return {'receita_em_reais': float(y_pred)}

