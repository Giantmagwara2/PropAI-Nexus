# src/agents/self_training/gnn_autoupdate_agent.py

import torch
import logging
from gnn_valuation import GNN
from torch_geometric.data import Data

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class GNNUpdateAgent:
    def __init__(self):
        self.model_save_path = "models/latest_gnn_model.pth"

    def retrain_gnn(self, data: Data):
        logger.info("🔁 Retraining GNN with latest data...")
        model = GNN()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
        criterion = torch.nn.MSELoss()

        model.train()
        for epoch in range(30):
            optimizer.zero_grad()
            output = model(data.x, data.edge_index)
            loss = criterion(output, data.y)
            loss.backward()
            optimizer.step()

            if epoch % 10 == 0:
                logger.info(f"Epoch {epoch} - Loss: {loss.item()}")

        torch.save(model.state_dict(), self.model_save_path)
        logger.info("✅ GNN Model retrained and saved.")

    def evaluate_new_model(self, data: Data, old_model_path: str):
        # (Optional) Compare new model vs old model using validation sets
        pass  # Coming soon 😎
