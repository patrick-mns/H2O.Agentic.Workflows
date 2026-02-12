# H2O Agentic Workflows

Repositório de teste para [GitHub Agentic Workflows (gh-aw)](https://github.com/github/gh-aw).

## O que é gh-aw?

GitHub Agentic Workflows permite escrever workflows automatizados em linguagem natural (Markdown) que rodam como GitHub Actions com agentes de IA (Copilot, Claude ou Codex).

## Uso

```python
from example import hello_world, soma

# Exemplo básico
print(hello_world())  # Output: Hello, World!

# Soma de números
resultado = soma(5, 3)
print(resultado)  # Output: 8
```

## Setup

```bash
# 1. Instalar a extensão gh-aw
gh extension install github/gh-aw

# 2. Verificar instalação
gh aw version

# 3. Inicializar o repositório
gh aw init --engine copilot

# 4. Compilar workflows
gh aw compile

# 5. Commit e push
git add .
git commit -m "Setup GitHub Agentic Workflows"
git push
```

## Workflows incluídos

| Workflow | Trigger | Descrição |
|----------|---------|-----------|
| `continuous-documentation.md` | PR, Push, Weekly, Manual | Mantém documentação sincronizada com código |

### Continuous Documentation

Workflow inteligente que:
- ✅ **Em PRs**: Verifica se mudanças no código incluem atualizações de documentação
- 📊 **Em Push (main)**: Audita toda a documentação do repositório
- 📅 **Semanalmente**: Gera relatório completo de saúde da documentação
- 💡 **Sempre**: Sugere melhorias específicas e identifica gaps de documentação

## Estrutura

```
.github/
└── workflows/
    ├── continuous-documentation.md      # Workflow de documentação contínua
    └── continuous-documentation.lock.yml # Workflow compilado (gerado)
```

## Referências

- [Documentação gh-aw](https://github.github.com/gh-aw/)
- [Quick Start](https://github.github.com/gh-aw/setup/quick-start/)
- [Workflow Structure](https://github.github.com/gh-aw/reference/workflow-structure/)
- [Frontmatter Reference](https://github.github.com/gh-aw/reference/frontmatter/)
