from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# 配置允许 ngrok 域名的安全策略
security = TransportSecuritySettings(
    enable_dns_rebinding_protection=False,
    allowed_hosts=["*"],
    allowed_origins=["*"],
)

mcp = FastMCP(
    "Test Server",
    json_response=True,
    host="0.0.0.0",
    port=8000,
    transport_security=security,
)

# ✅ 关键修复：给工具和参数添加完整描述
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    计算两个整数的和
    Args:
        a: 第一个要相加的整数
        b: 第二个要相加的整数
    Returns:
        两个整数相加的结果
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    计算两个整数的乘法
    Args:
        a: 第一个要乘法的整数
        b: 第二个要乘法的整数
    Returns:
        两个整数相乘的结果
    """
    return a * b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    return f"Write a {style} greeting for someone named {name}."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")