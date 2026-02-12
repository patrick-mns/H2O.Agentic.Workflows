# Contribuindo para H2O Agentic Workflows

Obrigado por considerar contribuir para este projeto! 🎉

## Como Contribuir

### Reportando Bugs

Se você encontrar um bug, por favor abra uma issue incluindo:

- Uma descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. comportamento atual
- Versão do Python e do gh-aw
- Sistema operacional

### Sugerindo Melhorias

Sugestões de melhorias são sempre bem-vindas! Por favor:

- Verifique se já não existe uma issue similar
- Descreva claramente a melhoria proposta
- Explique por que essa melhoria seria útil

### Pull Requests

1. **Fork o repositório** e crie sua branch a partir de `main`:
   ```bash
   git checkout -b feature/minha-contribuicao
   ```

2. **Faça suas alterações**:
   - Escreva código limpo e documentado
   - Adicione type hints em funções Python
   - Adicione docstrings seguindo o padrão do projeto
   - Siga o estilo de código existente

3. **Teste suas alterações**:
   ```bash
   python -m doctest example.py
   ```

4. **Atualize a documentação**:
   - Atualize o README.md se necessário
   - Adicione entrada no CHANGELOG.md na seção [Unreleased]
   - Documente novas funcionalidades

5. **Commit suas mudanças**:
   ```bash
   git commit -m "feat: adiciona nova funcionalidade"
   ```
   
   Use mensagens de commit descritivas seguindo [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` para novas funcionalidades
   - `fix:` para correções de bugs
   - `docs:` para mudanças na documentação
   - `refactor:` para refatorações
   - `test:` para adição ou modificação de testes

6. **Push para seu fork** e abra um Pull Request

### Padrões de Código

#### Python

- Use type hints em todas as funções
- Docstrings em português seguindo o formato Google
- Máximo de 100 caracteres por linha
- Use f-strings para formatação de strings

Exemplo:
```python
def funcao_exemplo(parametro: str) -> int:
    """
    Descrição breve da função.
    
    Args:
        parametro: Descrição do parâmetro
        
    Returns:
        Descrição do valor de retorno
    """
    return len(parametro)
```

#### Markdown

- Use formatação consistente
- Inclua exemplos quando relevante
- Mantenha links funcionais

### Workflow de Documentação

Este projeto usa GitHub Agentic Workflows para manter a documentação:

- A documentação é verificada automaticamente em PRs
- Mudanças no código devem incluir atualizações de documentação
- O workflow sugere melhorias quando gaps são detectados

### Processo de Review

1. Pelo menos um revisor deve aprovar o PR
2. Todos os checks automatizados devem passar
3. O código deve seguir os padrões estabelecidos
4. A documentação deve estar atualizada

### Código de Conduta

- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros

## Precisa de Ajuda?

- Abra uma issue com a tag `question`
- Entre em contato através das issues do GitHub

Obrigado por contribuir! 🚀
