import os

def duvida():

	while True:
		res = input('''\033[31mQuais São Suas Duvidas : ?\033[m\033[34m
[1 ] Olá python
[2 ] Números 
[3 ] Strings 
[4 ] Tuplas
[5 ] Listas
[6 ] Dicionários
[7 ] Sets
[8 ] Operadores de Comparação 
[9 ] if, Elif, Else 
[10] Loop For 
[11] Range 
[12] While
[13] Funções
[14] Programação Orientada à Objetos 
[15] Bibliotecas, e um dos melhores Canal aprender Python ? 
[16] Para voçê Sair do Chat \n ''' )

		if res == '1':
				print('''Hello, Python!
				Bem vindo ao Python
				São várias as características do Python que o tornam uma linguagem tão promissora e, 
				que atrai a cada dia, mais desenvolvedores. A seguir, foram elucidados alguma dessas 
				características e junto, uma breve descrição.

				• Fácil de aprender: O Python é uma linguagem fácil de ser aprendida e poderosa para trabalharmos. 
				A mesma possui uma sintaxe limpa e clara, como também, contém um conjunto de bibliotecas 
				estáveis e bem estruturadas.

				• Fácil leitura e compreensão: A sintaxe da linguagem é minimalista, isso é, mantém somente o necessário, 
				o que torna o código escrito, muitas vezes, a um texto em Inglês.

				• Fácil manutenção: Em decorrência da simplicidade sintática e da excelente estruturação das bibliotecas, 
				a manutenção de códigos, seja aquele que desenvolvemos ou mesmo de terceiros, muito mais fácil e compreensível.

				• Multiplataforma: O interpretador do Python é escrito com a Linguagem C e C++, assim, o mesmo pode ser 
				portado a todas as plataformas que possuam compiladores para a linguagem. Tendo em vista que o C++ 
				é a linguagem mais difundida e a base de praticamente toda a informática, temos compiladores 
				ou portados para quase todas as plataformas existentes.

				• Modo interativo: Sendo o Python uma linguagem interpretada, foi possível o desenvolvimento 
				de ferramentas interativas, isto é, ferramentas majoritariamente em linha de comando, onde podemos 
				executar instruções e analisar a saída.

				Hoje Python está presente nas áreas de Desenvolvimento Web, Inteligência Artificial, Computação Gráfica, 
				Big Data, Ciência de Dados e Muito Mais!

				Os tópicos aqui elucidados estão longe de esgotar os recursos do Python! Por essa razão, 
				continuaremos o nosso estudo sobre as principais características e 
				recursos da linguagem nos próximas seções.''')
		elif res == '2':
			print('''Números, Python tem vários tipos,de números literais,
			numéricos. 
			Nós nos concentraremos
			principalmente em números inteiros. int e
			números de ponto. flutuante float.
			Inteiros são apenas números inteiros,
			positivos ou negativos. Por exemplo: 2 e -2
			são exemplos de números inteiros.
			Os números de pontos flutuantes em Python
			são notáveis porque eles têm um ponto
			são exemplos de números de ponto flutuante.
			#4 E 2, 4 vezes 10 elevado a 2 também é um
			exemplo de um número de ponto flutuante
			em Python.
			Aqui está alguns exemplos dos dois tipos
			principais:
			1,2,-5, 1000 Inteiros ou int
			1.2,-0.5, 2 e 2, 3 E 2 Numero Ponto-flutuante ou
			float.
			Agora vamos ver algumas aritmética basica.

			Ex: Soma

			2+1

			3

			Subtração
			2 - 1
			1

			Multiplicaçã0
			2*2
			4
			Divisão, divisões sempre retornam um
			3 / 2
			1.5 ''')

		elif res == '3':
			
			print('''As strings são usadas em Python para registrar 
			informações de texto, como nomes ou frases. As strings em 
			Python são na verdade uma sequência, o que basicamente significa que o 
			Python acompanha cada elemento da string como uma sequência de caracteres. 
			exemplo, Python entende a string ,hello, como uma sequência de letras em 
			uma ordem específica. Isso significa que poderemos usar a indexação 
			para pegar letras particulares como a primeira letra ou a última letra.
			Para criar uma string em Python, você precisa usar aspas simples ou aspas 
			duplas. Por exemplo:
				
			1 palavra
			'hello'

			Uma frase inteira 
			'Isso também é uma string'
			Também é possível usar aspas duplas 
			"String com aspas duplas"
			'Isso também é uma string'
			'hello'
			'String com aspas simples'
			Imprimindo uma String
			Uma sequência de caracteres emitirá automaticamente 
			cadeias de caracteres, mas a maneira correta de exibir strings 
			na sua saída é usando uma função de impressão.

			Podemos simplismente declarar uma string

			'Hello World' Mas a maneira correta é utilizar o método print().

			print('Hello World 1') 
			Hello World

			print('Use \n para inserir uma nova linha')
			Use
			para inserir uma nova linha

			Nós também podemos usar uma função chamada len() para 
			verificar o comprimento de uma string!

			len('Hello World')

			print(len(Hello World))

			10 letras tem Hello Word

			H e  l   l   o  W o  r   l    d
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10

			Indexação em Strings
			Sabemos que as strings são uma sequência, o que significa que o 
			Python pode usar índices para chamar partes da sequência. 
			Vamos aprender como isso funciona.

			Em Python, usamos colchetes após um objeto para chamar seu índice. 
			Devemos também notar que a indexação começa em '0'para Python. 
			Vamos criar um novo objeto chamado "nome" e caminharmos 
			através de alguns exemplos de indexação.Sabemos que as strings 
			são uma sequência, o que significa que o Python pode usar índices 
			para chamar partes da sequência. Vamos aprender como isso funciona.

			exemplos de indexação.
			
			Define 'nome' como uma string

			nome = ('Aprendendo python') 

			Imprima o objeto

			print(nome)

			Aprendendo python

			Vamos começar a indexar!

			Mostra o primeiro elemento (neste caso uma letra)

			print(nome[0])
			'A'

			print(nome[1])
			'n'

			Podemos usar um dois pontos : para executar corte que pega 
			tudo até um ponto designado. Por exemplo:
				
			Retorna todos elementos a partir do elemento de índice 1

			print(nome[1:])
			Observe que não há mudanças no elemento 
			nome
			prendendo python

			Retorna tudo até o elemento de índice 12 
			print(nome[:13])
			Aprendendo py

			Observe o corte acima. Aqui, estamos dizendo ao Python que pegue tudo de 0 a 13. 
			Não inclui o 13° índice. Você notará muito isso em Python, 
			onde as declarações são geralmente até o contexto, mas não o incluindo.

			Também podemos usar indexação negativa para retroceder.
			Última letra (um índice antes do 0, então ele começa da parte de trás) 

			nome[-1]

			Pega tudo, menos a última letra 
			print(nome[:-1])
			Aprendendo pytho

			Também podemos usar notação de índice e fatia para capturar 
			elementos de uma sequência com espaçamentos (o espaçamento padrão é 1). 
			Por exemplo, podemos usar dois pontos em uma linha e, em seguida, 
			um número que especifica a frequência para capturar elementos. Por exemplo:

			Pega tudo, mas com passos negativos, de trás para frente. 
			print(nome[::-1])
			nohtyp odnednerpA

			Pega tudo, mas os espaçamentos são de 2 em 2 

			print([::2])
			arned yhn

			Pega tudo, de 1 em 1 
			print(nome[::1]
			Aprendendo python

			Essa idéia de uma sequência é importante em Python e nós vamos 
			abordá-la logo abaixo.Propriedades das Strings
			É importante notar que as strings têm uma propriedade importante 
			conhecida como imutabilidade. Isso significa que, uma vez que uma 
			string é criada, os elementos nela não podem ser alterados ou substituídos. 
			Por exemplo:

			nome = Aprendendo python

			Vamos tentar mudar a primeira letra para 'X' 

			nome[0] = 'X'
			---------------------------------------------------------------------------
			TypeError                                 Traceback (most recent call last) 
			<ipython-input-3-bf1b55f1477a> in <module>() 
			1 Vamos tentar mudar a primeira letra para 'x' 
			----> 2 s[0] = 'x' 
			---------------------------------------------------------------------------
			TypeError: 'str' é um objeto que nao pode se mudada, 
			o python  não podem alterar a atribuição do item!

			Algo que podemos fazer é concatenar strings!
			Aprendendo python

			Concatenar as strings 
			nome + ' concatenate me!'
			s = 'concatenate me!'
			Assim podemos redefinir completamente s 
			x = nome +'s'
			print(x)
			Aprendendo python concatenate me!

			Podemos usar o símbolo de multiplicação para criar repetições!   Aprender = 'z'

			aprender*10

			'zzzzzzzzzz'

			Métodos embutidos em strings
			Os objetos em Python geralmente possuem métodos internos. Esses métodos são 
			funções dentro do objeto que podem executar ações ou comandos no próprio objeto.

			Chamamos métodos com um ponto e depois o nome do método. Os métodos estão 
			na forma: objeto.método(parâmetros)

			Onde os parâmetros são argumentos extras que podemos passar para o método.

			Aqui estão alguns exemplos de métodos internos em strings


			nome = Aprendendo python

			Coloca toda string em maiuscula

			print(nome.upper())
			APRENDENDO PYTHON

			colocando a string em minuscula

			print(nome.lower())
			aprendendo python

			Divide uma string nos espaços em branco (este é o padrão) 

			print(nome.split())
			['Aprendendo', 'python']

			Divide em um elemento específico (não inclui o elemento que foi dividido) 

			(nome.split('A')
			[' ', 'prendendo python']

			Nesta seção, abordaremos brevemente as várias maneiras de formatar 
			suas declarações impressas. À medida que você codifica mais e mais, 
			você provavelmente deseja ter declarações de impressão que possam 
			incluir uma variável em uma declaração de string impressa.

			O exemplo mais básico de uma declaração de impressão é:
				
			Formatação de Impressão
			print('isso e uma string')

			Você pode usar o 'f' antes das aspas para formatar strings 
			em suas instruções de impressão.

			x = python

			print(f' Gostoei muito {x}, é uma liguagens muito boa')
			Gostoei muito python,é uma liguagens muito boa ''')


		elif res == '4':
			print('''Tuplas
			Em Python, as tuplas são muito semelhantes às listas, no entanto, 
			ao contrário das listas, elas são imutáveis, o que significa que elas não 
			podem ser alteradas. Você usaria tuplas para apresentar coisas que não 
			deveriam ser alteradas, como dias da semana ou datas em um calendário.

			Você terá uma intuição de como usar tuplas com base no que você sabe 
			sobre as listas. Nós podemos tratá-las de forma muito semelhante, 
			com a maior distinção é que as tuplas são imutáveis.
			Construindo Tuplas
			A construção de tuplas usa () com elementos separados por vírgulas. Por exemplo:

			Pode-se criar uma tupla com múltiplos elementos 
			t = (1,2,3)
			O método len() funciona também para tuplas 
			print(len(t))
			3
			Você também pode variar os tipos de dados
			t = ('one',2)
			print(t)
			('one', 2)

			E a indexação funciona exatamente como nas listas

			t[0]
			'one'

			Corte de dados também...
			t[-1]
			2

			Métodos básicos da Tupla:
			As tuplas têm métodos internos, mas não tantos quanto as listas. 
			Vamos ver dois deles:

			Use .index() com o valor de parâmetro para retornar o índice do mesmo
			t.index('one')
			0
			Use .count() para saber quantas vezes determinado elemento 
			apareceu na tupla
			t.count('one')
			1
			Exemplos:
			xt = ('arroz', 96,'ad', 3,'arroz')
			print(xt.index(3))
			print(xt.count('arroz'))

			Imutabilidade
			Como mencionado anteriormente, tuplas são imutáveis:
			Vamos adicionar um elemento a variavel:
			xt = ('arroz', 96,'ad', 3,'arroz')
			xt[0] = 'feijao'
			---------------------------------------------------------------------------
			TypeError                                 Traceback (most recent call last)
			<ipython-input-14-93def5f9b4bd> in <module>()
			----> 1 xt[0]= 'feijao'
			TypeError: 'tuple' o objeto 'feijao' não pode ser adicionando,
			---------------------------------------------------------------------------
			porque tuplas não podem ser alteradas
			por causa dessa imutabilidade, as tuplas não podem crescer. 
			Uma vez que uma tupla é feita, não podemos adicionar novos 
			elementos a ela.
			---------------------------------------------------------------------------
			xt.append('feijao')
			AttributeError                            Traceback (most recent call last)
			<ipython-input-15-799b3447c4d9> in <module>()
			----> 1 t.append('feijao')
			 ttributeError: 'tuple' object has no attribute 'append'
			---------------------------------------------------------------------------
			Então quando usar tuplas ?
			Você pode estar se perguntando:Por que se preocupar em usar tuplas quando 
			elas têm menos métodos disponíveis? 
			Para ser honesto, as tuplas não são usadas tantas vezes como listas na programação,
			mas são usadas quando a imutabilidade é necessária. Se no seu programa 
			você está passando por um objeto e precisa ter certeza de que ele não 
			seja alterado, então a tupla se tornará sua solução. Ela fornece uma fonte 
			conveniente de integridade de dados.
			Agora você pode criar e usar suas tuplas em sua programação, 
			bem como ter uma compreensão da sua imutabilidade.''')

		elif res == '5':
			print('''Listas Na seção Strings, introduzimos o conceito de 
			sequência em Python. 
			As listas podem ser pensadas na versão mais geral de uma sequência 
			Python. Ao contrário das strings, elas são mutáveis, o que significa 
			que os elementos dentro de uma lista podem ser alterados!

			Nesta seção, aprenderemos sobre:

			1. Criação de listas 
			2. Índice e corte de listas 
			3. Métodos básicos da lista 
			4. Listas aninhadas 

			As listas são construídas com colchetes e vírgulas que 
			separam cada elemento da lista. 

			Vamos Avançar e ver como podemos construir listas!

			A vamos criar um variavel e da um nome a ela
			my_list

			my_list = [1,2,3]

			Acabamos de criar uma lista de números inteiros, 
			mas as listas podem realmente armazenar diferentes 
			tipos de objeto. Por exemplo:my_list = ['string',23,100.232,'list']

			Assim como as strings, a função len() irá dizer 
			quantos itens estão na sequência da lista.
			print(len(my_list))
			4

			Indexação e corte

			Indexar e cortar funciona exatamente como em strings. 
			Vamos fazer uma nova lista para nos lembrar de como isso funciona:
				
			my_list = ['one','two','three',4,5]
			Pega o elemento de índice 0 
			print(my_list[0])
			'one'
			
			Pega o índice 1 e tudo depois 
			print(my_list[1:])
			['two', 'three', 4, 5]

			Pega tudo até o elemento de índice 3 
			print(my_list[:3])
			['one', 'two', 'three']

			Nós também podemos usar + para concatenar listas, 
			assim como fizemos com strings.
			my_list + ['new item']
			['one', 'two', 'three', 4, 5, 'new item']

			Nota: Isso realmente não altera a lista original!
			my_list
			['one', 'two', 'three', 4, 5]

			Você teria que reatribuir a lista para tornar a mudança permanente.
			Reatribuição 
			my_list = my_list + ['add new item permanently']
			my_list

			['one', 'two', 'three', 4, 5, 'add new item permanently']Nós também podemos usar o * para um método de duplicação semelhante às strings:
				
			Dobrar a lista 

			my_list * 2
			['one', 'two', 'three', 4, 5, 'add new item permanently', 'one', 'two', 'three', 4, 5, 'add new item permanentinetly']

			Métodos Básicos de Lista
			Se você está familiarizado com outra linguagem de programação, 
			você pode começar a comparar os arrays dessa linguagem com listas em Python. 
			As listas em Python, no entanto, tendem a ser mais flexíveis do que 
			arrays em outras linguagens por dois bons motivos: 
			elas não têm tamanho fixo o que significa que não precisamos 
			especificar o tamanho de uma lista,e elas não têm restrição
			de tipo fixo vomo já vimos acima. 

			Vamos prosseguir e explorar alguns métodos mais especiais para listas:
				
			Cria a lista 
			l = [1,2,3]

			Use o método append() para adicionar permanentemente um item ao 
			final de uma lista:
			Acresentar 
			l.append('append me!')
			Mostrar 
			l[1, 2, 3, 'append me!']

			Use pop() para "retirar" um item da lista. Por padrão, 
			pop tira o último índice, mas também pode-se especificar 
			qual índice irá retirar. Vamos ver um exemplo:
				
			Retira o item de índice 0 permanentemente 
			l.pop(0)
			1
			Mostrar 
			l
			[2, 3, 'append me!']
			Atribui o elemento retirado, lembre-se de que o índice padrão é -1 
			popped_item = l.pop()
			'append me!'
			Mostra a lista restante 
			l

			Também deve notar-se que a indexação das listas 
			retornará um erro se não houver nenhum elemento nesse índice. 
			Por exemplo:
			l[100]
			---------------------------------------------------------------------------
			IndexError                                Traceback # #  # (most recent call last)
			<ipython-input-11-e2a0c2623844> in # <module>()
			----> 1 l[100]

			IndexError: list index out of range
			---------------------------------------------------------------------------

			Podemos usar os métodos sort() e reverse() para alterar as listas:
				
			new_list = ['a','e','x','b','c']
			new_list
			['a', 'e', 'x', 'b', 'c']

			Use o reverse() para reverter a ordem (isto é permanente!)
			
			new_list.reverse()['c', 'b', 'x', 'e', 'a']

			Use sort() para classificar a lista (neste caso, ordem alfabética) 
			new_list.sort()
			new_list
			['a', 'b', 'c', 'e', 'x']

			Listas aninhadas
			Uma ótima característica das estruturas de dados do Python 
			é que elas suportam aninhamento. Isso significa que podemos 
			ter estruturas de dados dentro das estruturas de dados. 
			Por exemplo: uma lista dentro de uma lista.

			Vamos ver como isso funciona!

			Começamos com 3 listas
			lst_1 = [1,2,3]
			lst_2 = [4,5,6]
			lst_3 = [7,8,9]

			Faça uma lista de listas para formar uma matriz

			print(matrix = [lst_1, lst_2, lst_3])
			[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

			Agora, podemos usar novamente a indexação para pegar elementos, 
			mas agora existem dois níveis para o índice. Os itens no objeto 
			matriz e, em seguida, os itens dentro dessa lista!

			Pega o primeiro item no objeto da matriz
			matrix[0]
			Pega o primeiro item do primeiro item no objeto da matrix

			print(matrix[0][0])
			1
			print(matrix)[1][3])
			6
			Tudo que vimos foi listas, nunca devemos esquecer,lista podem ser alteradas mais as tuplas não...''')

		elif res == '6':

			print('''Dicionários
			Nas seções anteriores temos aprendido sobre sequências em Python, mas agora vamos mudar de 
			engrenagem e aprender sobre mapeamentos em Python. Se você está familiarizado com outras linguagens, 
			pode pensar nestes Dicionários como tabelas de hash.

			Então, o que são os mapeamentos? Os mapeamentos são 
			uma coleção de objetos que são armazenados por uma chave, 
			ao contrário de uma sequência que armazena objetos por sua 
			posição relativa. Esta é uma distinção importante, 
			uma vez que os mapeamentos não reterão a ordem, 
			pois possuem objetos definidos por uma chave.

			Um dicionário de Python consiste em uma chave e depois 
			em um valor associado. Esse valor pode ser quase qualquer objeto Python.
			Construindo um Dicionário
			Vamos ver como podemos construir dicionários para obter 
			uma melhor compreensão de como eles funcionam!

			Cria um dicionário com {} e: que significa uma chave e um valor
			my_dict = {'key1':'value1','key2':'value2'}
			Chamando valores pela chave
			my_dict['key2']
			'value2'

			É importante notar que os dicionários são muito flexíveis com relação 
			aos tipos de dados que eles podem conter. Por exemplo:
			my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
			Vamos chamar itens do dicionário
			my_dict['key3']
			['item0', 'item1', 'item2']
			Podemos chamar itens de uma lista presente na posição referente à chave: 
			key3

			my_dict['key3'][0]
			'item0'

			Podemos chamar métodos nos itens também

			my_dict['key3'][0].upper()
			'ITEM0'

			Podemos também alterar valores através da chave.
			my_dict['key1'] = 123
			my_dict['key1'] = my_dict['key1'] - 123
			my_dict['key1'] = 0

			Uma nota rápida: o Python possui um método interno de fazer 
			uma subtração ou adição automática (ou multiplicação ou divisão). 
			Poderíamos ter usado += ou -= para a atribuição. Por exemplo:

			Define o objeto como sendo ele mesmo menos 123

			my_dict['key1'] -= 123
			my_dict['key1'] -123

			Também podemos criar chaves por atribuição. Por exemplo,
			se começássemos com um dicionário vazio, poderíamos adicionar-lhe 
			continuamente:


			Cria um novo dicionário
			d = {}

			Cria uma chave por associoação
			d['animal'] = 'Dog'
			Pode fazer isso com qualquer objeto
			d['Prefido'] = 42
			print(d)
			{'animal': 'Dog', 'preferido': 42}

			Aninhamento de dicionários
			Espero que você esteja começando a ver o quão poderoso Python 
			é com sua flexibilidade de objetos de nidificação e métodos dos mesmos. 
			Vamos ver um dicionário aninhado dentro de um dicionário:

			d = {'key1':{'nestkey':{'subnestkey':'value'}}}

			Continue chamando as chaves...
			d['key1']['nestkey']['subnestkey']
			'value'
			Alguns métodos de dicionários:

			Existem alguns métodos que podemos chamar em um dicionário.
			Vamos começar uma breve introdução a alguns deles:
			Cria um dicionário típico

			d = {'key1':1,'key2':2,'key3':3}

			Retorna uma lista de todas as chaves 
			d.keys()
			['key3', 'key2', 'key1']
			[3, 2, 1]

			Método para retornar, as tuplas de todos os itens
			d.items()
			
			Espero que você tenha agora um bom entendimento 
			básico para a construção de dicionários. 
			Há muito mais para explorar aqui. Depois desta seção, 
			tudo o que você precisa saber é como criar um dicionário 
			e como recuperar seus valores.''')

		elif res == '7':
			print('''Sets os conjuntos(sets) são uma coleção não ordenada 
			de elementos únicos. Podemos construí-los usando a 
			função set(). vamos fazer um conjunto para ver como funciona.
			x = set()
			Adicionamos elementos com o método add()
			x.add(1)
			print(x)
			{1}

			Observe as chaves. Isso não indica um dicionário! 
			Embora você possa montar analogias como um set 
			sendo um dicionário com apenas chaves. 
			Sabemos que um conjunto tem apenas entradas únicas. 
			Então, o que acontece quando tentamos adicionar 
			algo que já está em um conjunto?

			Adiciona um elemento novo
			x.add(2)
			print(x.add(2))
			x{1, 2}
			Adiciona o mesmo elemento
			print(x.add(1))
			{1, 2}

			Observe como ele não colocará mais 1 lá. 
			Isso porque um conjunto apenas se ocupa de elementos exclusivos! 
			Podemos transformar uma lista com múltiplos elementos repetidos 
			para um conjunto para obter os elementos exclusivos. Por exemplo:

			Cria uma lista com elementos repetidos
			lz = [1,1,2,2,3,4,5,6,1,1]

			Transforma em um set com elementos únicos
			print(set(lz))
			{1, 2, 3, 4, 5, 6}

			Agora você já sabe como usar set() em seu código, 
			lembre-se de usá-los quando você precisar de elementos não repetidos. ''')


		elif res == '8':
			print('''Operadores de comparação Nesta seção estaremos 
			aprendendo sobre Operadores de Comparação em Python. 
			Esses operadores nos permitirão comparar variáveis 
			e produzir um valor booleano Verdadeiro ou Falso
			Se você tiver alguma base em Matemática, 
			esses operadores devem ser muito diretos.
			Em primeiro lugar, apresentaremos uma tabela dos operadores 
			de comparação e depois trabalharemos com alguns exemplos:

			Tabela de operadores de comparação
			Operador:
			# ==
			Descrição:
			Se os valores de dois operandos forem
			iguais, a condição torna-se verdadeira.

			Exemplo:
			# (a==b) não é verdade.

			Operador:
			#. !=
			Descrição:
			Se valores de dois operandos não
			forem iguais, a condição torna-se

			# (a!= b) é verdadeiro

			Operador
			# >

			Descrição:
			Se o valor do operando esquerdo forr
			maior que o valor do operando direito,
			condição torna-se verdadeira.
			# (a>b) não é verdadeiro

			Operador:
			# <

			Descrição:
			Se o valor do operando esquerdo forr
			inferior ao valor do operando direito, a
			condição torna-se verdadeira.

			Exemplo:
			# (a<b) é verdadeiro.

			Operador:
			# >=

			Descrição:
			Se o valor do operando esquerdo forr
			maior ou igual ao valor do operando
			direito, a condição torna-se verdadeira.

			Exemplo:
			# (a>=b) não é verdadeiro.

			Operador:
			# <= 

			Descrição:
			Se o valor do operando esquerdo forr
			menor ou igual ao valor do operando
			direito, a condição torna-se verdadeira.

			Exemplo:
			# (a=b) é erdadeiro

			Vamos agora trabalhar com exemplos rápidos de cada um desses.

			Igualdade
			# 2 == 2
			# True (verdadeiro)
			# 1 == 0
			# False (falso)

			Desigualdade
			# 2 != 1
			# True
			# 2!= 2
			# False

			Maior que
			# 2 > 1
			# True
			# 2 > 4
			# False

			Menor que
			# 2 < 4
			# True
			# 2 < 1
			# False

			Maior ou igual que
			# 2 >= 2
			# True
			# 2 >= 1
			# True

			Menor ou igual que
			# 2 <= 2
			# True
			# 2 <= 4
			# True

			Operadores de comparação em cadeia
			Uma característica interessante do Python é a capacidade de encadear 
			comparações múltiplas para realizar um teste mais complexo. 
			Você pode usar essas comparações em cadeia como uma abreviatura 
			para expressões booleanas maiores.

			# Agora, aprenderemos como encadear operadores de comparação e também 
			# apresentamos duas outras declarações importantes em Python: and e or .

			Vejamos alguns exemplos de uso de cadeias:
			# 1 < 2 < 3
			# True

			# A declaração acima verifica se 1 era inferior a 2 e se 2 era inferior a 3. 
			# Poderíamos ter escrito isso usando a instrução and em Python:
			# 1<2 and 2<3True

			# O and é usado para garantir que as duas verificações tenham que ser verdadeiras 
			# para que a verificação total seja verdadeira. Vamos ver outro exemplo:
			# 1 < 3 > 2
			# True

			# As verificações acima checam se 3 é maior do que os outros números. 
			# Você pode usar and para reescrevê-lo como:
			# 1<3 and 3>2
			# True

			# É importante notar que o Python está verificando ambas as instâncias 
			# das comparações. Nós também podemos usar or para escrever comparações em Python. 

			Por exemplo:
			# 1==2 or 2<3
			# True

			# Observe como a expressão retornou True porque com o operador or precisamos 
			# apenas que um dos dois sejam verdadeiros. Outro exemplo:
			# 1==1 or 100==1
			# True  ''')

		elif res == '9':
			print('''if, elif else são declarações condicionais que fornecem 
			a tomada de decisão necessária quando você 
			deseja executar o código com base em uma condição específica.
			if = "Se acontecer isso execute alguma ação" 
			Podemos então expandir a idéia com declarações 
			que nos permite contar ao computador:
			elif "Caso contrário,se aquilo acontecer, execute alguma outra ação"
			else "se nenhum dos casos acima acontecer, excute esta ação"
			
			Vamos avançar e ver o formato de 
			Sintaxe para as instruções if para ter uma idéia melhor disso:

				if pista1:
					executar ação 1
				elif pista2:
					execute ação 2
				else:pista3
					execute a ação 3 
			
			Exemplos:
			vamos viajar
			pista1 = (1)
			pista2 = (2)
			pista3 = (3)
			qual písta vamos pegar?
			1 2 ou 3

			if resp == 1:
				print(' vão chegar mais tarde ')
				
			elif resp == 2:
				print(' vão chegar mais cedo')
			else:
				print('não vão viajar')
			Exemplos:    
			vamos pegar a pista1
			vão chegar mais tarde!

			Então vamos pegar a pista2
			vão chegar mais cedo!

			Não queremos a pista3
			então não vão viajar!

			Exemplo2:
			Vamos criar dois exemplos mais simples para as afirmações if, elif e else:
			pessoa = 'josycreide'

			if pessoa == 'josycreide':
				print('bem vinda josycreide!')
			else:
				print('bem vinda, qual seu nome?')
			bem vinda Josycreide!

			pessoa = 'Snoop'

			if pessoa == 'josycreide':
				print('bem vinda josycreide!')
			elif pessoa =='snoop':
				print('bem vindo Snoop!")
			else:
				print('bem vindo,qual seu nome?')
			
			bem vinda josycreide!
			bem vindo Snoop!
			bem vindo,qual seu nome

			Agora você já sabe como criar estruturas de decisão no seu código, isso será muito útil 
			para quando o programa deve se comportar de determinada forma dependendo da situação. ''')

		elif res == '10':
			print('''For: Um loop que atua como um iterador em Python, ele passa por 
			itens que estão em uma sequência ou qualquer outro item iterável.
			Os objetos que aprendemos até agora que podemos iterar incluem 
			strings, listas, tuplas e até iteráveis embutidos 
			em dicionários, como chaves ou valores.

			Já vimos for um pouco nas seções anteriores, mas agora permitimos 
			formalizar a nossa compreensão.

			Aqui está o formato geral para um for loop em Python:

				for item in objeto:
					fazer algo

			O nome da variável usado para o item fica a seu critério, 
			você pode escolher o que quiser. Então use seu melhor julgamento 
			para escolher um nome que faça sentido e que você poderá entender 
			ao revisar seu código. Este nome do item pode então ser referenciado 
			dentro de seu loop, por exemplo, se você quisesse usar instruções 
			
			if para executar verificações.

			Vamos seguir em frente e trabalhar com vários exemplos de 
			for loops usando uma variedade de tipos de objetos de dados. 
			Vamos começar com um exemplo simples e adicionar mais 
			complexidade ao decorrer da seção.For

			Um loop for atua como um iterador em Python, ele passa por itens 
			que estão em uma sequência ou qualquer outro item iterável. Os objetos 
			que aprendemos até agora que podemos iterar incluem strings, listas, tuplas 
			e até iteráveis embutidos em dicionários, como chaves ou valores.

			Exemplos
			Iterando através de uma lista.
			y = [1,2,3,4,5,6,7,8,9,10]
			for num in y:
				print(num)
			1
			2
			3
			4
			5
			6
			7
			8
			9
			10

			Exemplo2
			aqui com o comando end=' ', o loop fica na mesma linha,print(num, end=' ') ele serve pra 
			finalizar a saida do codigo, assim o computador entederar que pode por o resultado, na mesma linha.
			y = [1,2,3,4,5,6,7,8,9,10]
			for num in y:
				print(num,end=' ')
			1 2 3 4 5 6 7 8 9 10

			Ótimo! Espero que isso tenha feito sentido. Agora, vamos adicionar uma instrução 
			if para verificar se há números pares. Vamos utilizar o módulo.

			Vamos imprimir apenas os números pares dessa lista
			for num in y:
				if num % 2 == 0:
					print(num,end=' ')
			2 4 6 8 10

			for num in y:
					if num % 2 == 0:
					print(num)
				else:
					print('Número ímpar')
			Número ímpar
			2
			Número ímpar
			4
			Número ímpar
			6
			Número ímpar
			8
			Número ímpar
			10

			Outra idéia comum durante um for é manter algum tipo 
			de contagem durante os vários loops. Por exemplo, 
			vamos criar um loop for que resume a lista:
			y2 = 10 
			for num in y:
				y2 = y2 + num
			print(y2)
			65

			Ótimo! Leia sobre a célula acima e certifique-se de entender completamente o 
			que está acontecendo. aqui somamos todos os objetos da lista y, e somamos 
			mais o valor da lista y2.Também poderíamos ter implementado um += para a adição. 

			Por exemplo:
			y = 0 
			for num in y:
				y2 += num
			print(y2)
			55

			Nós usamos for com listas, e as strings? Lembre-se de que as strings 
			são uma sequência, então, quando iteramos através delas, estaremos 
			acessando cada item nessa sequência de caracteres.For
			Nós usamos for com listas, e as strings? Lembre-se de que as strings 
			são uma sequência, então, quando iteramos através delas, estaremos 
			acessando cada item nessa sequência de caracteres.
			55
			list_sum = 0 

			for num in l:
				list_sum += num

			print(list_sum)
			for letter in ' Isso e uma string.':
				print(letter)
			I
			s
			s
			o
			
			e

			u
			m
			a

			s
			t
			r
			i
			n
			g
			.
			E com tuplas ?

			tup = (1,2,3,4,5)

			for t in tup:
				print(t)tup = (1,2,3,4,5)

			for t in tup:
				print(t)
			1
			2
			3
			4
			5

			As Tuplas têm uma qualidade especial quando se trata de fors. 
			Se você está iterando através de uma sequência que contém tuplas, 
			o item pode realmente ser a própria tupla, este é um exemplo de desembalagem de tuplas. 
			Durante o for, estaremos desembalando a tupla dentro de uma sequência e podemos acessar 
			os itens individuais dentro dessa tupla!

			xy = [(2,4),(6,8),(10,12)]
			(2, 4)
			(6, 8)
			(10, 12)
			for tup in xy:
				print(tup) 
			 
			Agora desembalando
			for (t1,t2) in l:
				print(t1)
			2
			6
			10

			Com as tuplas em uma sequência, podemos acessar os itens dentro delas por meio de desembalagem! 
			A razão pela qual isso é importante é porque muitos objetos entregarão seus iteradores através de tuplas. 
			Vamos começar a explorar a iteração através de Dicionários para explorar isso ainda mais!

			d = {'k1':1,'k2':2,'k3':3}
			for item in d:
				print(item)
			k3
			k2
			k1

			Observe como isso produz apenas chaves. Então, como podemos obter os valores? 
			Ou as chaves e os valores?
			Você deve usar items() para iterar através das chaves e valores de um dicionário. 
			Por exemplo:Observe como isso produz apenas chaves. Então, como podemos obter os valores? 
			Ou as chaves e os valores?

			Você deve usar items() para iterar através das chaves e valores de um dicionário. Por exemplo:
			for k,v in d.items():
				print(k)
				print(v)

			k3
			3
			k2
			2
			k1
			1

			Conclusão:

			Aprendemos a usar for para iterar através de tuplas, listas, strings e dicionários. 
			Será uma ferramenta importante para nós, portanto, certifique-se de conhecê-lo bem e 
			compreende os exemplos acima.!''')

		elif res == '11':

			print('''Range Nesta seção estaremos discutindo a função range(). 
			Vamos conhecer esta simples função (mas extremamente útil!).
			range() nos permite criar uma sequência de números que variam de um ponto de partida até um ponto final. 
			Também podemos especificar o tamanho do passo. Vamos percorrer alguns exemplos:
			range(0, 10)
			Perceba como a função não produziu a lista, isso acontece porque devemos informar ao Python 
			que queremos que o range() seja convertido para uma lista. Podemos usar a função list() 
			para fazer isso, vamos tentar de novo mas agora usando essa função:

			range(0, 10)
			(list(range(0,10))
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

			Vamos tentar outro exemplor = range(10,25)
			Podemos usar a função tuple() se quisermos uma tupla em vez de uma lista 
			tuple(r)
			(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

			Podemos também especificar o tamanho do passo na sequência com um terceiro argumento. Vamos ver um exemplo:
			r = range(0, 20, 2)

			print('list(r)')
			[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

			Outra grande vantagem do range() é que podemos iterar sobre ele em um for.

			Exemplos:
			for i in range(0,10): >>>>> O (i) voçê pode subistituir ela variavel que quiser 
				print(i)
			0
			1
			2
			3
			4
			5
			6
			7
			8
			9

			for i in range(0,10): 
				print( i , end=',') >>>>>>>>> Quando acrescentamos o end='' ,falamos pro contador por na mesma linha o loop.

			0,1,2,3,4,5,6,7,8,9

			Impressionante, não é? Esses são apenas alguns exemplos do que podemos fazer com o range()


			for c in range(0, 10, 2): >>>contador vai de 0 a 10 pulando de 2 em 2, quando queremos isso,
			so adicionar outro numero
			0, 2, 4, 6, 8  ''')

		elif res == '12':
			print('''while...
			A instrução while em Python é uma das formas mais gerais de executar iterações. 
			Uma instrução while executará repetidamente uma única declaração ou grupo de instruções, 
			desde que a condição seja verdadeira. A razão pela qual é chamado de "loop" é porque as instruções 
			de código são rodadas repetidamente até que a condição não seja mais atendida.

			O formato geral de um loop while é:


			x = 0
			while x < 10: >>>>>>> equanto x for menor que 10, continua o loop
			print('x e atualmente é: ', x)
			print ('x ainda é menor que 10, adicionando 1 a x')
			x += 1


			x é atualmente: 0
			x é x ainda é menor que 10, adicionando 1 a x
			x é atualmente: 1
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 2
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 3
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 4
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 5
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 6
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 7
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 8
			  x é x ainda é menor que 10, adicionando 1 a x
			 x é atualmente: 9
			  x é x ainda é menor que 10, adicionando 1 a x

			Observe quantas vezes as declarações de impressão ocorreram e como o while continuou 
			até a condição True deixasse de ser verdadeira, que ocorreu quando x passou a ser 10. 
			É importante notar que, uma vez que isso ocorreu, o código parou. Vamos ver como podemos 
			adicionar uma outra afirmação:


			x = 0
			while x < 10:
			 	print('x é ainda menos de 10')
				if x == 3:
					print(' parei porque x == 3')
					break >>>>>>>>>>>> siguifica que o loop para aqui,ou seja eu quero que seja aqui !!!
				else:
					print('continua...')
					continue


			x é ainda menos de 10, adicionando 1 a x
			continua...


			x é ainda menos de 10, adicionando 1 a x
			continua...

			x é ainda menos de 10, adicionando 1 a x
			continua...

			Parando porque x == 3

			Observe como a declaração else não foi alcançada e a continuação nunca foi impressa! 
			Após esses exemplos breves e simples, você deve se sentir confortável ao usar as instruções em seu código.

			Uma observação importante! É possível criar um ciclo de execução infinita com instruções while. Por exemplo:

			v = infinito
			while True:
				print(v) ''')

		elif res == '13':

			print('''Funções
			Introdução às Funções
			Esta seção consistirá em explicar o que é uma função em Python e como criar uma. As funções 
			serão um dos nossos principais blocos de construção quando construirmos quantidades 
			maiores e maiores de código para resolver problemas.

			Então, o que é uma função ?

			Formalmente, uma função é um dispositivo útil que agrupa um conjunto de instruções 
			para que elas possam ser executadas mais de uma vez. Elas também podem nos permitir especificar 
			parâmetros que possam servir como entradas para as funções.

			Em um nível mais fundamental, as funções nos permitem não ter que repetidamente escrever 
			o mesmo código repetidas vezes. Se você lembrar das lições em strings e listas, 
			lembre-se de que usamos uma função len() para obter o comprimento de uma string. 
			Uma vez que verificar o comprimento de uma sequência é uma tarefa comum, você 
			provavelmente vai querer escrever uma função que pode fazer isso repetidamente.

			As funções serão um dos níveis mais básicos de código de reutilização em Python, e também nos permitirá 
			começar a pensar no design do programa.def = definição é o parametro que comoça todas as funções
			Vamos ver como construir a sintaxe de uma função em Python. Ela tem a seguinte forma:

			def minha_funcao(arg1,arg2):
				
					A documentação da função ficará aqui (seu codigo)
				
				Faça coisas aqui (o que voçê quer quer a função executa .!!!!)
				return  retorne o resultado desejado aqui

			Começamos com def, seguido do nome da função. Tente manter os nomes relevantes, 
			por exemplo len() é um bom nome para uma função length. Também tenha cuidado com os nomes, 
			você não gostaria de chamar uma função do mesmo nome que uma função interna em Python (como len).

			Em seguida, vem um par de parênteses com vários argumentos separados por uma vírgula. 
			Esses argumentos são as entradas para sua função. Você poderá usar essas entradas em sua função e 
			fazer referência a elas. Depois disso, você coloca dois pontos.

			Agora, aqui é o passo importante, você deve identar para começar o código dentro de sua função corretamente. 
			Python faz uso de espaço em branco para organizar o código. Muitas outras linguagens de programação não 
			fazem isso, então tenha isso em mente.

			Em seguida, você verá o doc-string, é aqui que você escreve uma descrição básica da função. 
			Documentações não são necessárias para funções simples, mas é uma boa prática colocá-las 
			para que você ou outras pessoas possam facilmente entender o código que você escreve.

			Depois de tudo isso, você começa a escrever o código que deseja executar.

			A melhor maneira de aprender funções é através de exemplos. Então, vamos tentar passar por exemplos 
			que se relacionam com os vários objetos e estruturas de dados que aprendemos antes.

			Importante sempre que for usar a função te que chamar Ela:
			exemplo:

			def executar(): >>> sem paramentro() vazio
				print('Estou')

			executar()
			print('gostando de aprender pyhton')

			executar()
			print('gostando de programação')

			def diga_ola():
				print('Ola')
			diga_ola()
			ola

			Vamos escrever uma função que comprimenta pessoas com seu nome.


			def comprimentar(name):>>>>>> com paramentro (name) 
				print(f'ola, {name}')
			comprimentar('Rodrigo')
			ola, Rodrigo

			Usando o return:

			Vamos ver um exemplo que usa uma declaração de retorno. A instrução return permite que uma função 
			retorne um resultado que pode ser armazenado em uma variável por exemplo, ou usado de qualquer outra maneira.

			def soma(num1, num2):
				return num1+num2
			soma(4, 5)
			9
			resultado = soma(4,5)
			print(resultado)
			9

			O que acontece se inserimos duas strings?

			print(soma('one','two'))
			onetwo

			Note, porque não declaramos tipos de variáveis em Python, esta função pode ser usada 
			para adicionar números ou sequências em conjunto.

			Finalmente, vamos passar por um exemplo completo de criar uma função para verificar se um número é primo.

			Nós sabemos que um número é primo se esse número é apenas divisível em 1 e em si mesmo. 
			Vamos escrever a nossa primeira versão da função para verificar todos os números 
			de 1 a N e executar verificações de módulo.def e_primo(num):

				Método para checar se é primo
				
				for n in range(2,num):
					if num % n == 0:
						print('Não é primo')
						break
				else:  Se o módulo nunca for zero, é primo
					print('Primo')
			Não é primo

			e_primo(16)

			Observe como quebramos o código após a declaração de impressão! Na verdade, podemos melhorar isso ao 
			verificar somente a raiz quadrada do número-alvo, também podemos ignorar todos os números pares 
			depois de verificar 2. Também mudaremos para retornar um valor booleano para obter 
			um exemplo de usar declarações de retorno:

			import math >>>>>>> é uma biblioteca do python tem a seção sobre elas,e como fuciona

			def e_primo(num):

			Melhor método para checar primos

			if num % 2 == 0 and num > 2: 
				return False
			for i in range(3, int(math.sqrt(num)) + 1, 2):
				if num % i == 0:
					return False
			return Trueis_prime(11)
			True

			Ótimo! Você deve agora ter uma compreensão básica sobre como criar suas próprias funções para 
			salvar-se de escrever repetidamente o código!")
					
			Declarações aninhadas e Escopo

			Agora que passamos a escrever nossas próprias funções, é importante entender como o 
			Python lida com os nomes das variáveis que você atribui. Quando você cria um nome de variável em Python, 
			o nome é armazenado em um namespace. Nomes de variáveis também têm escopo. 
			O escopo determina a visibilidade desse nome de variável para outras partes do seu código,
			nunca use espaço em nome de funções,subistitua com uma 'underline _' .

			Comece com uma rápida experiência de pensamento, imagine o seguinte código:

			x = 25

			def imprimir():
				x = 50
				return 
				
			O que você imagina que print() printarar? 25 ou 50? Qual é o resultado da impressão x? 25 ou 50?
			print(x)
			25
			print(imprimir())
			50
			Interessante! Mas como o Python sabe qual x você está se referindo no seu código? 
			Este é o lugar onde a idéia de escopo vem. Python tem um conjunto de regras que segue para decidir 
			quais variáveis (como x neste caso) você está fazendo referência em seu código. Vamos investigar as regras:

			Essa idéia de escopo em seu código é muito importante entender para atribuir e chamar 
			nomes de variáveis ​​adequadamente.

			Em termos simples, a idéia de escopo pode ser descrita por 3 regras gerais:

				1. As atribuições de nomes criam ou alteram nomes locais por padrão.

				2. Existem 4 possíveis tipos escopos. São eles:
					local
					enclosing functions
					global
					built-in

				3. Os nomes declarados em declarações globais e não locais mapeiam nomes atribuídos 
				para preencher módulos e escopos de função.

			A declaração em 2 acima pode ser definida pela regra LEGB.

			Regra LEGB.

			L: Local - Nomes atribuídos de qualquer forma dentro de uma função (def ou lambda) 
			e declarações não globais nessa função.

			E: Enclosing function locals - Nome no escopo local de todas e quaisquer funções 
			encapsuladas (def ou lambda), de dentro para fora.

			G: Global (módulo) - Nomes atribuídos no nível superior de um arquivo de módulo, 
			ou declarados como global em um def dentro do arquivo.

			B: Built-in (Python) - Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...def local():
				x é local aqui
				x = 10
				print(x)

			local()
			10
			Local
			def local():
				a = 100
				print(locals())

			local()

			Podemos usar a função locals() para retornar um dicionário com todas as variáveis locais.
			'a': 100
			Enclosing function locals
			Isso ocorre quando temos uma função dentro de uma função (funções aninhadas).

			name = 'este e um nome global'

			def greet():
				name = 'Sammy'

				def ola():
					print('ola ' + name)

				ola()

			cumprimentar()
			print(name)  ola Sammy
			este e um nome global

			Observe como Sammy foi usado, porque a função ola() foi anexada dentro da função de 
			saudação!
			
			Global

			Variáveis globais são visíveis em todo o código. Podemos usar a função globals() 
			para retornar um dicionário com todas as variáveis globais.

			var_global = "Variável global"
			print(var_global)
			Variável global 

			print(globals())
			'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': class 
			'_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__':  '__builtins__': 
			<module 'builtins' (built-in)>, 'x': 25, 'local': <function local at 0x01B8C660>,
			'name': 'This is a global name', 'greet': <function greet at 0x01E9E978>, 'var_global': 'Variável global'

			Built-in
			Built-in são os nomes de funções incorporados no Python (não substitua-os!).
			len
			<built-in function len>

			Variáveis Locais
			Quando você declara variáveis dentro de uma definição de função, elas não estão relacionadas 
			de nenhuma maneira a outras variáveis com os mesmos nomes usados fora da função. Ou seja, 
			os nomes de variáveis são locais para a função. Isso é chamado de escopo da variável. 
			Todas as variáveis têm o escopo do bloco em que são declarados a partir do ponto de definição do nome.

			Exemplo:
			x = 50

			def func(x):
				print('x is', x)
				x = 2
				print('Changed local x to', x)

			func(x)
			print('x is still', x)x is 50
			Changed local x to 2
			x is still 50

			Na primeira vez que imprimimos o valor do nome x com a primeira linha no corpo da função, 
			o Python usa o valor do parâmetro declarado no bloco principal, acima da definição da função.

			Em seguida, atribuímos o valor 2 a x. O nome x é local para nossa função. Então, quando mudamos 
			o valor de x na função, o x definido no bloco principal permanece inalterado.

			Com a última declaração de impressão, mostramos o valor de x conforme definido no bloco principal, 
			confirmando assim que ele não é afetado pela atribuição local dentro da função anteriormente chamada.
			A declaração global
			Se você deseja atribuir um valor a um nome definido no nível superior do programa 
			(ou seja, não dentro de qualquer tipo de escopo, como funções ou classes), então você deve dizer ao 
			Python que o nome não é local, mas é global. Fazemos isso usando a declaração global. 
			É impossível atribuir um valor a uma variável definida fora de uma função sem a declaração global.

			Você pode usar os valores de tais variáveis ​​definidas fora da função (assumindo que não há nenhuma 
			variável com o mesmo nome dentro da função). No entanto, isso não é encorajado e deve ser evitado, 
			uma vez que não fica claro para o leitor do programa como a definição daquela variável. 
			O uso da declaração global torna claro que a variável é definida em um bloco mais externo.

			Exemplo:x = 50

			def func():
				global x
				print('This function is now using the global x!')
				print('Because of global x is:', x)
				x = 2
				print('Ran func(), changed global x to', x)

			print('Before calling func(), x is:', x)
			func()
			print('Value of x (outside of func()) is:', x)
			Before calling func(), x is: 50
			This function is now using the global x!
			Because of global x is: 50
			Ran func(), changed global x to 2
			Value of x (outside of func()) is: 2A declaração global é usada para declarar que x é uma variável global, 
			portanto, quando atribuímos um valor a x dentro da função, essa alteração é refletida quando 
			usamos o valor de x no bloco principal.

			Você pode especificar mais de uma variável global usando a mesma declaração global separando-as por vírgula, 
			exemplo: global x, y, z.

			Conclusão
			Você deve agora ter um bom entendimento sobre o Escopo. Uma última menção é que você pode usar as 
			funções globals() e locals() para verificar quais são suas variáveis locais e globais.

			Outra coisa a ter em mente é que tudo em Python é um objeto! Eu posso atribuir variáveis com funções 
			como eu posso com números ou strings! ''')

		
			print('''Programação orientada a objetos
			A Programação Orientada a Objetos (POO) tende a ser um dos principais obstáculos para iniciantes
			quando começam a aprender Python.

			Para esta seção vamos construir nosso conhecimento de POO em Python, abordando os seguintes tópicos:

				• Objetos
				• Usando a palavra-chave class
				• Criando atributos de classe
				• Criando métodos em uma classe
				• Herança
				• Métodos especiais para classes

			Vamos começar lembrando sobre os objetos básicos do Python. Por exemplo:
			l = [1,2,3]

			Lembre-se de como podemos chamar métodos em uma lista?
			l.count(2) = 1

			O que vamos fazer basicamente é explorar como podemos criar um tipo de objeto como uma lista. 
			Já aprendemos sobre como criar funções. Então, vamos explorar objetos em geral.

			Objetos :

			Em Python, tudo é um objeto. Podemos usar a função type() para verificar o tipo do objeto:

			print(type(1))
			print(type([{}]))
			print(type(()))
			print(type())
			<class 'int'>
			<class 'list'>
			<class 'tuple'>
			<class 'dict'>

			Então sabemos que em Python tudo é um objeto, então, como podemos criar nossos próprios tipos de objetos? 
			É aí que entra a palavra-chave class.

			classclass:
			A classe é um modelo que define a natureza de um objeto. Das classes podemos construir instâncias. 
			Uma instância é um objeto específico criado a partir de uma determinada classe. Por exemplo, acima, 
			criamos o objeto "l" que era uma instância de um objeto da classe lista.

			Vamos ver como podemos usar a palavra-chave class:

			Cria um novo tipo de objeto chamado Exemplo:

			class Exemplo(object):
				pass

			Instanciando Exemplo
			x = Exemplo()

			print(type(x))

			class '__main__.Exemplo'>

			Por convenção damos às classes um nome que começa com uma letra maiúscula. 
			Observe como x é agora a referência para nossa nova instância da classe Exemplo. 
			Em outras palavras, nós instanciamos a classe Exemplo.

			Dentro da classe temos apenas um pass(que é usado quando queremos que algo não faça nada). 
			Mas podemos definir atributos e métodos para a classe.

			Um atributo é uma característica de um objeto. Um método é uma operação que podemos realizar com o objeto.

			Por exemplo, podemos criar uma classe chamada Dog. Um atributo de Dog pode ser sua raça ou seu nome, 
			enquanto um método para Dog pode ser algo como latir() que retorna um som.

			Vamos ter uma melhor compreensão dos atributos através de um exemplo.Atributos
			A sintaxe para criar um atributo é:

				self.attribute = algo

			Existe um método especial chamado: __init__()

			Esse método é usado para inicializar os atributos de um objeto. Por exemplo:

			class cachorro(object):
				def __init__(self, raça):
					self.raça = raça

			Ale = cachorro(raça ='Labrador')
			sammy = cachorro(raça ='Huskie')

			Vamos descrever o que temos acima. O método especial __init__() é 
			chamado automaticamente logo após o objeto ter sido criado:

			def __init__ (self, raça): Cada atributo em uma definição de classe começa com uma referência ao 
			objeto de instância. É convencionalmente chamado de self(semelhante ao "this" em outras linguagens). 
			raça é o argumento. O valor é passado durante a instanciação da classe.

			Agora criamos duas instâncias da classe cachorro. Com dois tipos de raças, podemos acessar estes 
			atributos assim:sammy.raça
			'Huskie'
			Ale.raça
			'labrador'

			Observe como não temos parênteses após breed, isto é porque é um atributo e não leva nenhum argumento.

			Em Python também existem atributos de objeto de classe. Esses atributos são os mesmos para qualquer 
			instância da classe. Por exemplo, podemos criar o atributo especie para a classe Dog. 
			Os cães independentemente da sua raça, nome ou outros atributos serão sempre mamíferos. 
			Aplicamos essa lógica da seguinte maneira:class Dog(object):

				Atributos da classe

				species = 'animal'

				def __init__(self, raça, name):
					self.raça = raça
					self.name = name
			Ale = cachoro('Labrador','Sammy')
			sammy.name
			'Sammy'

			Observe que o Atributo da Classe foi definido fora de qualquer método na classe. 
			Também por convenção, nós os colocamos antes do __init__().
			sam.species
			'animal'

			Métodos
			Métodos são funções definidas dentro do corpo de uma classe. Eles são usados para executar 
			operações com os atributos de nossos objetos. Os métodos são essenciais no conceito de encapsulamento em POO. 
			Isso é essencial para dividir as responsabilidades na programação, especialmente em grandes aplicações.

			Você pode basicamente pensar em métodos como funções que atuam em um Objeto que levam o próprio 
			Objeto através de seu argumento self.

			Vamos passar por um exemplo de criação de uma classe Circle:class Circle(object):
				
				pi = 3.14

				O círculo é instanciado com um raio (o padrão é 1)
					def __init__(self, radius=1):
					self.radius = radius 

				Método de cálculo da área. Observe o uso de self.
				def area(self):
					return self.radius * self.radius * Circle.pi

				Método que redefine o raio
				def setRadius(self, radius):
					self.radius = radius

				Método para obter o raio
				def getRadius(self):
					return self.radius


			c = Circle()

			c.setRadius(2)
			print('O raio é:', c.getRadius())
			print('A área é:', c.area())

			O raio é: 2
			A área é: 12.56Ótimo! Observe como nós usamos a notação self para atributos de referência da
			classe dentro dos métodos.

			Herança
			A herança é uma forma de formar novas classes usando classes que já foram definidas. 
			As classes recém formadas são chamadas classes derivadas, as classes de que derivamos 
			são chamadas de classes base. Os benefícios importantes da herança são a reutilização 
			de códigos e a redução da complexidade de um programa. As classes derivadas (descendentes) 
			substituem ou estendem a funcionalidade das classes base (ancestrais).

			Vejamos um exemplo incorporando nosso trabalho anterior na classe cachorro:

			class Animal(object):
				def __init__(self):
					print("Animal criada")

				def quem_sou_eu(self):
					print("Animal")

				def comer(self):
					print("comendo")


			class cachorro(Animal):
				def __init__(self):
					Animal.__init__(self)
					print("cachorro criado")

				def quem_sou_eu(self):
					print("cachorro")

				def latido(self):
					print("Woof!")d = cachorro()
			Animal criado
			cachorro criado
			d.quem_sou_eu()
			cachorro
			comendo
			d.comer()
			d.latido()
			Woof!

			Neste exemplo, temos duas classes: Animal e cachorro. O animal é a classe base, o cachorro é a classe derivada.

			A classe derivada herda a funcionalidade da classe base.

				• É mostrado pelo método quem_sou_eu(). A classe derivada modifica o comportamento existente da classe base.

				• É mostrado pelo método comer(). Finalmente, a classe derivada estende a funcionalidade da classe base, 
			e também define um novo método latir()

			Métodos especiais
			Finalmente, vamos dar uma olhada em métodos especiais. Classes em Python podem implementar 
			determinadas operações com nomes de métodos especiais. Esses métodos não são realmente chamados diretamente, 
			mas pela sintaxe de linguagem específica do Python. Por exemplo, vamos criar uma classe Book:
			class livro(objetor):
				def __init__(self, titlo, autor, paginas):
					print("o livro foi criado")
					self.title = titlo
					self.author = autor
					self.pages = paginas

				def __str__(self):
					return "Titlo:%s, autor:%s, paginas:%s " %(self.titlo, self.autor, self.paginas)

				def __len__(self):
					return self.paginas

				def __del__(self):
					print("o livro foi destruido")
			livro = livro("Python Rocks!", "Rodrigo Tadewald", 159)

			Métodos especiais
			print(livro)
			print(len(livro))
			apague livro
			o livro foi criado

			Titulo:Python Rocks!, autor:Rodrigo Tadewald, paginas:159 
			159

			o livro foi destruido

			Os métodos init(), str(), len() e del() são definidos pelo uso de sublinhados. 
			Eles nos permitem usar funções específicas do Python em objetos criados através da nossa classe.

			Ótimo! Após esta seção, você deve ter uma compreensão básica de como criar seus próprios 
			objetos com classe em Python.''')


		elif res == '14':
			print('''Programação orientada a objetos
			A Programação Orientada a Objetos (POO) tende a ser um dos principais obstáculos para iniciantes
			quando começam a aprender Python.

			Para esta seção vamos construir nosso conhecimento de POO em Python, abordando os seguintes tópicos:

				• Objetos
				• Usando a palavra-chave class
				• Criando atributos de classe
				• Criando métodos em uma classe
				• Herança
				• Métodos especiais para classes

			Vamos começar lembrando sobre os objetos básicos do Python. Por exemplo:
			l = [1,2,3]

			Lembre-se de como podemos chamar métodos em uma lista?
			l.count(2) = 1

			O que vamos fazer basicamente é explorar como podemos criar um tipo de objeto como uma lista. 
			Já aprendemos sobre como criar funções. Então, vamos explorar objetos em geral.

			Objetos :

			Em Python, tudo é um objeto. Podemos usar a função type() para verificar o tipo do objeto:

			print(type(1))
			print(type([]))
			print(type(()))
			print(type())
			<class 'int'>
			<class 'list'>
			<class 'tuple'>
			<class 'dict'>

			Então sabemos que em Python tudo é um objeto, então, como podemos criar nossos próprios tipos de objetos? 
			É aí que entra a palavra-chave class.

			classclass:
			A classe é um modelo que define a natureza de um objeto. Das classes podemos construir instâncias. 
			Uma instância é um objeto específico criado a partir de uma determinada classe. Por exemplo, acima, 
			criamos o objeto "l" que era uma instância de um objeto da classe lista.

			Vamos ver como podemos usar a palavra-chave class:

			Cria um novo tipo de objeto chamado Exemplo:

			class Exemplo(object):
				pass

			Instanciando Exemplo
			x = Exemplo()

			print(type(x))

			class '__main__.Exemplo'>

			Por convenção damos às classes um nome que começa com uma letra maiúscula. 
			Observe como x é agora a referência para nossa nova instância da classe Exemplo. 
			Em outras palavras, nós instanciamos a classe Exemplo.

			Dentro da classe temos apenas um pass(que é usado quando queremos que algo não faça nada). 
			Mas podemos definir atributos e métodos para a classe.

			Um atributo é uma característica de um objeto. Um método é uma operação que podemos realizar com o objeto.

			Por exemplo, podemos criar uma classe chamada Dog. Um atributo de Dog pode ser sua raça ou seu nome, 
			enquanto um método para Dog pode ser algo como latir() que retorna um som.

			Vamos ter uma melhor compreensão dos atributos através de um exemplo.Atributos
			A sintaxe para criar um atributo é:

				self.attribute = algo

			Existe um método especial chamado: __init__()

			Esse método é usado para inicializar os atributos de um objeto. Por exemplo:

			class cachorro(object):
				def __init__(self, raça):
					self.raça = raça

			Ale = cachorro(raça ='Labrador')
			sammy = cachorro(raça ='Huskie')

			Vamos descrever o que temos acima. O método especial __init__() é 
			chamado automaticamente logo após o objeto ter sido criado:

			def __init__ (self, raça): Cada atributo em uma definição de classe começa com uma referência ao 
			objeto de instância. É convencionalmente chamado de self(semelhante ao "this" em outras linguagens). 
			raça é o argumento. O valor é passado durante a instanciação da classe.

			Agora criamos duas instâncias da classe cachorro. Com dois tipos de raças, podemos acessar estes 
			atributos assim:sammy.raça
			'Huskie'
			Ale.raça
			'labrador'

			Observe como não temos parênteses após breed, isto é porque é um atributo e não leva nenhum argumento.

			Em Python também existem atributos de objeto de classe. Esses atributos são os mesmos para qualquer 
			instância da classe. Por exemplo, podemos criar o atributo especie para a classe Dog. 
			Os cães independentemente da sua raça, nome ou outros atributos serão sempre mamíferos. 
			Aplicamos essa lógica da seguinte maneira:class Dog(object):

				Atributos da classe

				species = 'animal'

				def __init__(self, raça, name):
					self.raça = raça
					self.name = name
			Ale = cachoro('Labrador','Sammy')
			sammy.name
			'Sammy'

			Observe que o Atributo da Classe foi definido fora de qualquer método na classe. 
			Também por convenção, nós os colocamos antes do __init__().
			sam.species
			'animal'

			Métodos
			Métodos são funções definidas dentro do corpo de uma classe. Eles são usados para executar 
			operações com os atributos de nossos objetos. Os métodos são essenciais no conceito de encapsulamento em POO. 
			Isso é essencial para dividir as responsabilidades na programação, especialmente em grandes aplicações.

			Você pode basicamente pensar em métodos como funções que atuam em um Objeto que levam o próprio 
			Objeto através de seu argumento self.

			Vamos passar por um exemplo de criação de uma classe Circle:class Circle(object):
				
				pi = 3.14

				O círculo é instanciado com um raio (o padrão é 1)
					def __init__(self, radius=1):
					self.radius = radius 

				Método de cálculo da área. Observe o uso de self.
				def area(self):
					return self.radius * self.radius * Circle.pi

				Método que redefine o raio
				def setRadius(self, radius):
					self.radius = radius

				Método para obter o raio
				def getRadius(self):
					return self.radius


			c = Circle()

			c.setRadius(2)
			print('O raio é:', c.getRadius())
			print('A área é:', c.area())

			O raio é: 2
			A área é: 12.56Ótimo! Observe como nós usamos a notação self para atributos de referência da
			classe dentro dos métodos.

			Herança
			A herança é uma forma de formar novas classes usando classes que já foram definidas. 
			As classes recém formadas são chamadas classes derivadas, as classes de que derivamos 
			são chamadas de classes base. Os benefícios importantes da herança são a reutilização 
			de códigos e a redução da complexidade de um programa. As classes derivadas (descendentes) 
			substituem ou estendem a funcionalidade das classes base (ancestrais).

			Vejamos um exemplo incorporando nosso trabalho anterior na classe cachorro:

			class Animal(object):
				def __init__(self):
					print("Animal criada")

				def quem_sou_eu(self):
					print("Animal")

				def comer(self):
					print("comendo")


			class cachorro(Animal):
				def __init__(self):
					Animal.__init__(self)
					print("cachorro criado")

				def quem_sou_eu(self):
					print("cachorro")

				def latido(self):
					print("Woof!")d = cachorro()
			Animal criado
			cachorro criado
			d.quem_sou_eu()
			cachorro
			comendo
			d.comer()
			d.latido()
			Woof!

			Neste exemplo, temos duas classes: Animal e cachorro. O animal é a classe base, o cachorro é a classe derivada.

			A classe derivada herda a funcionalidade da classe base.

				• É mostrado pelo método quem_sou_eu(). A classe derivada modifica o comportamento existente da classe base.

				• É mostrado pelo método comer(). Finalmente, a classe derivada estende a funcionalidade da classe base, 
			e também define um novo método latir()

			Métodos especiais
			Finalmente, vamos dar uma olhada em métodos especiais. Classes em Python podem implementar 
			determinadas operações com nomes de métodos especiais. Esses métodos não são realmente chamados diretamente, 
			mas pela sintaxe de linguagem específica do Python. Por exemplo, vamos criar uma classe Book:
			class livro(objetor):
				def __init__(self, titlo, autor, paginas):
					print("o livro foi criado")
					self.title = titlo
					self.author = autor
					self.pages = paginas

				def __str__(self):
					return "Titlo:%s, autor:%s, paginas:%s " %(self.titlo, self.autor, self.paginas)

				def __len__(self):
					return self.paginas

				def __del__(self):
					print("o livro foi destruido")
			livro = livro("Python Rocks!", "Rodrigo Tadewald", 159)

			Métodos especiais
			print(livro)
			print(len(livro))
			apague livro
			o livro foi criado

			Titulo:Python Rocks!, autor:Rodrigo Tadewald, paginas:159 
			159

			o livro foi destruido

			Os métodos init(), str(), len() e del() são definidos pelo uso de sublinhados. 
			Eles nos permitem usar funções específicas do Python em objetos criados através da nossa classe.

			Ótimo! Após esta seção, você deve ter uma compreensão básica de como criar seus próprios 
			objetos com classe em Python.''')

		elif res == '15':
			
			print('''('https://docs.python.org/3/')
				(' https://www.cursoemvideo.com/course/python-3-mundo-1/ ')
				(' http://www.youtube.com/cursoemvideo ')
				(' https://docs.python.org/pt-br/3/library/math.html#module-math ')
            
            Para voçê abrir os links..preciona Ctrl com a seta do mouse no link,\ne vai em open ou abrir Boa Sorte !!!!''')

            
		
		elif res == '16':
			print('''Obrigado(a) !!!, Volte Sempre !!! e Até a próxima,se não tirei sua dúvida,\n 
            da uma olhada no chat [16],ou dar uma navegada no Google !!!\n
            Lembre-se conhecimento nunca é demais,boa Sorte!!!''')
			break
		else:
			print(' Número errado, tenta outra vez: ')
		
	

		
def loguin():
	print('\033[31mOlá! Bem Vindo(a) ChatBot !!! Aqui vou ajudar voçê, com suas Dúvidas !!!\033[m')
	nome = input(' \033[32mQual é o seu Nome: ?  ')
	Idade = input(' \033[32mDigite sua Idade: ? ')
	
loguin()
duvida()