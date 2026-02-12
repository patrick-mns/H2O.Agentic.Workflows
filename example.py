"""
Exemplo de módulo Python para demonstração.
"""

def hello_world() -> str:
    """Retorna uma saudação."""
    return "Hello, World!"


def soma(a: int | float, b: int | float) -> int | float:
    """
    Soma dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        A soma de a e b
    """
    return a + b
