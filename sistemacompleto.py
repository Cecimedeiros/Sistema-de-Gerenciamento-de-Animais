from first_crud import main1, carregar_abrigo, atualizar_abrigo, buscar_abrigos, excluir_abrigo, cadastrar_abrigo, listar_abrigo, fim
from sec_crud import carregar_animais, atualizar_animal, buscar_animal, excluir_animal, cadastrar_animal, main2, carregar_voluntario, buscar_voluntario, cadastrar_voluntario, excluir_voluntario, listar_animais, listar_voluntario, atualizar_voluntario
from third_crud import carregar_adotantes, cadastrar_adotante, atualizar_adotante, buscar_adotante, excluir_adotante, listar_adotantes, main3

carregar_abrigo ()
cadastrar_abrigo ('nome', 'endereco', 'porte_animal', 'contato')
listar_abrigo()
atualizar_abrigo('nome_antigo', 'novo_nome', 'novo_ende', 'novo_porte_animal','novo_contato')
excluir_abrigo ('nome')
buscar_abrigos('nome')
fim ()

carregar_voluntario()
cadastrar_voluntario('nome', 'cpf','endereco','horas')
listar_voluntario ()
excluir_voluntario('nome')
buscar_voluntario('nome')
atualizar_voluntario('nome_antigo','novo_nome', 'novo_ende', 'novo_contato', 'novo_horario' )

carregar_animais()
cadastrar_animal('nome', 'especie','idade', 'porte', 'raca', 'historico_medico')
listar_animais()
atualizar_animal('nome_antigo', 'novo_nome', 'nova_especie', 'nova_idade', 'novo_dono')
excluir_animal('nome')
buscar_animal('nome')
main2()

carregar_adotantes ()
cadastrar_adotante ('nome', 'idade', 'cidade', 'contato', 'preferencia_animal')
listar_adotantes()
buscar_adotante('nome')
atualizar_adotante('nome_velho', 'nome_novo', 'end_novo_adotante', 'porte_novo_escolhido','novo_contato_adotante')
excluir_adotante('nome')
main3()

main1()

