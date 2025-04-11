class PropertyEvaluatorAgent:
    def __init__(self, model):
        self.model = model
        self.features = model.feature_names_in_

    def predict(self, input_dict):
        import pandas as pd
        input_df = pd.DataFrame([input_dict])
        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=self.features, fill_value=0)
        prediction = self.model.predict(input_df)
        return prediction[0]
