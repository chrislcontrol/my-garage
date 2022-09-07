#!/bin/bash

# Valor default é execução web.
if [[ -z "${PROCESS_TYPE}" ]]; then
    PROCESS_TYPE="web"
fi

# Captura a linha de execução de migração de dados.
line_migrate=$(grep migrate: Procfile)

# Caso existir linha de comando para migração de dados, a mesma é executada.
if [[ ! -z line_migrate ]]; then
    command_migrate=${line_migrate#*:}
    echo "Running <migrate>: ${command_migrate}"
    eval ${command_migrate}
fi

# Captura a linha de geração de arquivos estáticos.
line_collectstatic=$(grep collectstatic: Procfile)

# Caso existir linha de comando para geração dos arquivos, a mesma é executada.
if [[ ! -z line_collectstatic ]]; then
    command_collectstatic=${line_collectstatic#*:}
    echo "Running <collectstatic>: ${command_collectstatic}"
    eval ${command_collectstatic}
fi

# Captura a linha de compilação da tradução.
line_compilemessages=$(grep compilemessages: Procfile)

# Caso existir linha de comando para compilar a tradução, a mesma é executada.
if [[ ! -z line_compilemessages ]]; then
    command_compilemessages=${line_compilemessages#*:}
    echo "Running <compilemessages>: ${command_compilemessages}"
    eval ${command_compilemessages}
fi

echo "Process type selected: ${PROCESS_TYPE}"

# Captura a linha de execução no procfile.
line_command=$(grep ${PROCESS_TYPE}: Procfile)
command=${line_command#*:}

echo "Running <$PROCESS_TYPE>: $command"
eval ${command}
