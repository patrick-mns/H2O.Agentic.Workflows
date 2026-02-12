# H2O Agentic Workflows

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/h2o-innovation/H2O.Agentic.Workflows/continuous-documentation.lock.yml)](https://github.com/h2o-innovation/H2O.Agentic.Workflows/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

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

## Troubleshooting

### Problemas Comuns

#### `gh aw: command not found`

**Solução**: Certifique-se de que a extensão gh-aw está instalada:
```bash
gh extension install github/gh-aw
gh extension list  # Verifica se gh-aw está na lista
```

#### Erro ao compilar workflows

**Problema**: `gh aw compile` falha com erro de permissão ou arquivo não encontrado.

**Solução**: 
1. Verifique se você está no diretório raiz do repositório
2. Confirme que a estrutura `.github/workflows/` existe
3. Tente executar com debug habilitado:
```bash
gh aw compile --verbose
```

#### Workflow não está executando

**Problema**: O workflow foi compilado mas não aparece nas Actions.

**Solução**:
1. Verifique se o arquivo `.lock.yml` foi commitado
2. Confirme os triggers no frontmatter do arquivo `.md`
3. Verifique se há erros no arquivo YAML compilado
4. Teste manualmente: `gh workflow run continuous-documentation.lock.yml`

#### Python não encontra o módulo `example`

**Problema**: `ModuleNotFoundError: No module named 'example'`

**Solução**: Execute o Python no diretório correto:
```bash
cd /caminho/para/H2O.Agentic.Workflows
python -c "from example import hello_world; print(hello_world())"
```

### Requisitos do Sistema

- **gh CLI**: Versão 2.0.0 ou superior
- **Python**: Versão 3.8 ou superior
- **Git**: Versão 2.0.0 ou superior
- **Permissões**: Acesso de escrita ao repositório para workflows

### Obtendo Ajuda

Se você encontrar um problema não listado aqui:

1. Verifique as [issues abertas](https://github.com/h2o-innovation/H2O.Agentic.Workflows/issues)
2. Consulte a [documentação do gh-aw](https://github.github.com/gh-aw/)
3. Abra uma nova issue com:
   - Descrição do problema
   - Passos para reproduzir
   - Saída de erro completa
   - Versões do gh CLI, Python e sistema operacional

## Referências

- [Documentação gh-aw](https://github.github.com/gh-aw/)
- [Quick Start](https://github.github.com/gh-aw/setup/quick-start/)
- [Workflow Structure](https://github.github.com/gh-aw/reference/workflow-structure/)
- [Frontmatter Reference](https://github.github.com/gh-aw/reference/frontmatter/)
