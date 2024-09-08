import pytest
from core.redis_client import redis_client

def test_redis_client_set_and_get():
    redis_client.set("test_key", "test_value")
    value = redis_client.get("test_key")
    assert value.decode('utf-8') == "test_value"
