from dataclasses import dataclass

@dataclass
class InferenceConfig:
    model_id: str = 'us.anthropic.claude-sonnet-4-6'
    max_tokens: int = 2048
    temperature: float = 0.7
    timeout: int = 30
    retries: int = 3
    region: str = 'us-east-1'
