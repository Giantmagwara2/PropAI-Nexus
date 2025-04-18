# src/agents/agent_hub.py

import asyncio

class AgentHub:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent_instance):
        """
        Register a new agent with the hub.
        """
        self.agents[name] = agent_instance
        print(f"✅ Registered agent: {name}")

    async def send_message(self, sender_name, receiver_name, message_type, payload):
        """
        Send a message between agents.
        """
        if receiver_name not in self.agents:
            raise Exception(f"Receiver agent {receiver_name} not found.")

        receiver = self.agents[receiver_name]
        response = await receiver.receive_message(sender_name, message_type, payload)
        return response
