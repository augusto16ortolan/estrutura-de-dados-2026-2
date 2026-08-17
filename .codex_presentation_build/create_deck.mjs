import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const OUT = "/Users/augustoortolan/Documents/aulas/2026:2/estrutura-de-dados-2026-2/trabalho-avaliativo-estrutura-de-dados-python.pptx";
const BUILD = "/Users/augustoortolan/Documents/aulas/2026:2/estrutura-de-dados-2026-2/.codex_presentation_build";

const W = 1280;
const H = 720;
const C = {
  dark: "#0E413C",
  teal: "#016663",
  white: "#FFFFFF",
};

const pres = Presentation.create({ slideSize: { width: W, height: H } });

function shape(slide, geometry, left, top, width, height, opts = {}) {
  return slide.shapes.add({
    geometry,
    position: { left, top, width, height },
    fill: opts.fill ?? "none",
    line: opts.line ?? { style: "solid", fill: "none", width: 0 },
    ...opts.extra,
  });
}

function text(slide, value, left, top, width, height, style = {}, name = undefined) {
  const box = slide.shapes.add({
    geometry: "textbox",
    name,
    position: { left, top, width, height },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  box.text = value;
  box.text.style = {
    fontFace: "Aptos",
    fontSize: 24,
    color: C.dark,
    ...style,
  };
  return box;
}

function footer(slide, n) {
  shape(slide, "rect", 0, H - 18, W, 18, { fill: C.dark });
  text(slide, String(n).padStart(2, "0"), W - 92, H - 45, 50, 22, {
    fontSize: 14,
    bold: true,
    color: C.teal,
    alignment: "right",
  });
}

function titleSlide(title, subtitle, meta) {
  const slide = pres.slides.add();
  slide.background.fill = C.white;
  shape(slide, "rect", 0, 0, 420, H, { fill: C.dark });
  shape(slide, "rect", 420, 0, 22, H, { fill: C.teal });
  text(slide, "ESTRUTURA DE DADOS", 64, 82, 290, 28, {
    fontSize: 16,
    bold: true,
    color: C.white,
    characterSpacing: 1,
  });
  text(slide, title, 486, 112, 650, 170, {
    fontSize: 54,
    bold: true,
    color: C.dark,
  });
  text(slide, subtitle, 490, 314, 610, 78, {
    fontSize: 26,
    color: C.teal,
  });
  text(slide, meta, 490, 540, 640, 58, {
    fontSize: 20,
    color: C.dark,
  });
  shape(slide, "rect", 1084, 0, 196, 22, { fill: C.teal });
  return slide;
}

function contentSlide(title, eyebrow = "") {
  const slide = pres.slides.add();
  slide.background.fill = C.white;
  shape(slide, "rect", 0, 0, W, 34, { fill: C.dark });
  shape(slide, "rect", 0, 34, 255, 8, { fill: C.teal });
  if (eyebrow) {
    text(slide, eyebrow.toUpperCase(), 72, 62, 760, 26, {
      fontSize: 14,
      bold: true,
      color: C.teal,
      characterSpacing: 1,
    });
  }
  text(slide, title, 72, 94, 1080, 52, {
    fontSize: 36,
    bold: true,
    color: C.dark,
  });
  footer(slide, pres.slides.items.length);
  return slide;
}

function sectionSlide(title, subtitle, number) {
  const slide = pres.slides.add();
  slide.background.fill = C.dark;
  shape(slide, "rect", 0, 0, W, H, { fill: C.dark });
  shape(slide, "rect", 0, 0, 86, H, { fill: C.teal });
  text(slide, String(number).padStart(2, "0"), 126, 104, 110, 62, {
    fontSize: 44,
    bold: true,
    color: C.white,
  });
  text(slide, title, 126, 205, 820, 110, {
    fontSize: 50,
    bold: true,
    color: C.white,
  });
  text(slide, subtitle, 130, 340, 780, 74, {
    fontSize: 25,
    color: C.white,
  });
  shape(slide, "rect", 1048, 0, 232, 22, { fill: C.white });
  footer(slide, pres.slides.items.length);
  return slide;
}

function bulletsSlide(title, eyebrow, bullets, opts = {}) {
  const slide = contentSlide(title, eyebrow);
  const intro = opts.intro;
  let top = 178;
  if (intro) {
    text(slide, intro, 72, 160, 1030, 56, { fontSize: 24, color: C.teal });
    top = 244;
  }
  const cols = opts.cols ?? 1;
  const colW = cols === 2 ? 520 : 960;
  const gap = 52;
  bullets.forEach((b, i) => {
    const col = cols === 2 ? i % 2 : 0;
    const row = cols === 2 ? Math.floor(i / 2) : i;
    const x = 92 + col * (colW + gap);
    const y = top + row * (opts.rowH ?? 58);
    shape(slide, "rect", x - 20, y + 8, 8, 24, { fill: C.teal });
    text(slide, b, x, y, colW, opts.itemH ?? 42, {
      fontSize: opts.fontSize ?? 24,
      color: C.dark,
    });
  });
  return slide;
}

function tableSlide(title, eyebrow, headers, rows, widths) {
  const slide = contentSlide(title, eyebrow);
  const left = 72;
  const top = 172;
  const rowH = 44;
  const totalW = widths.reduce((a, b) => a + b, 0);
  shape(slide, "rect", left, top, totalW, rowH, { fill: C.dark });
  let x = left;
  headers.forEach((h, i) => {
    text(slide, h, x + 12, top + 10, widths[i] - 24, 24, {
      fontSize: 18,
      bold: true,
      color: C.white,
    });
    x += widths[i];
  });
  rows.forEach((r, idx) => {
    const y = top + rowH + idx * rowH;
    shape(slide, "rect", left, y, totalW, rowH, {
      fill: idx % 2 === 0 ? C.white : "#F3FAF9",
      line: { style: "solid", fill: "#D6E7E5", width: 1 },
    });
    let cx = left;
    r.forEach((cell, i) => {
      text(slide, cell, cx + 12, y + 10, widths[i] - 24, 24, {
        fontSize: 18,
        color: C.dark,
        bold: i === 0,
      });
      cx += widths[i];
    });
  });
  return slide;
}

function twoColumnSlide(title, eyebrow, leftTitle, leftItems, rightTitle, rightItems) {
  const slide = contentSlide(title, eyebrow);
  const top = 180;
  const boxW = 510;
  [
    [72, leftTitle, leftItems],
    [698, rightTitle, rightItems],
  ].forEach(([x, h, items]) => {
    shape(slide, "rect", x, top, boxW, 46, { fill: C.teal });
    text(slide, h, x + 22, top + 10, boxW - 44, 26, {
      fontSize: 22,
      bold: true,
      color: C.white,
    });
    items.forEach((item, i) => {
      const y = top + 76 + i * 56;
      shape(slide, "rect", x, y + 8, 8, 24, { fill: C.teal });
      text(slide, item, x + 24, y, boxW - 40, 38, {
        fontSize: 21,
        color: C.dark,
      });
    });
  });
  return slide;
}

function flowSlide(title, eyebrow, steps) {
  const slide = contentSlide(title, eyebrow);
  const left = 94;
  const top = 232;
  const w = 185;
  steps.forEach((s, i) => {
    const x = left + i * 220;
    shape(slide, "roundRect", x, top, w, 116, {
      fill: i % 2 === 0 ? C.dark : C.teal,
      line: { style: "solid", fill: "none", width: 0 },
      extra: { borderRadius: "rounded-lg" },
    });
    text(slide, String(i + 1), x + 16, top + 12, 32, 30, {
      fontSize: 21,
      bold: true,
      color: C.white,
    });
    text(slide, s, x + 18, top + 50, w - 36, 48, {
      fontSize: 18,
      bold: true,
      color: C.white,
      alignment: "center",
    });
    if (i < steps.length - 1) {
      text(slide, ">", x + w + 14, top + 38, 32, 44, {
        fontSize: 36,
        bold: true,
        color: C.teal,
        alignment: "center",
      });
    }
  });
  return slide;
}

function checklistSlide(title, eyebrow, items) {
  const slide = contentSlide(title, eyebrow);
  items.forEach((item, i) => {
    const col = i < Math.ceil(items.length / 2) ? 0 : 1;
    const row = col === 0 ? i : i - Math.ceil(items.length / 2);
    const x = col === 0 ? 92 : 664;
    const y = 176 + row * 47;
    shape(slide, "ellipse", x, y + 2, 28, 28, {
      fill: C.teal,
      line: { style: "solid", fill: "none", width: 0 },
    });
    text(slide, "✓", x + 5, y + 2, 20, 24, {
      fontSize: 18,
      bold: true,
      color: C.white,
      alignment: "center",
    });
    text(slide, item, x + 42, y, 475, 32, {
      fontSize: 19,
      color: C.dark,
    });
  });
  return slide;
}

function codeBlockSlide(title, eyebrow, code, opts = {}) {
  const slide = contentSlide(title, eyebrow);
  if (opts.note) {
    text(slide, opts.note, 72, 154, 1040, 40, {
      fontSize: 22,
      color: C.teal,
    });
  }
  const top = opts.note ? 208 : 170;
  const box = shape(slide, "rect", 92, top, 1000, opts.height ?? 408, {
    fill: C.dark,
    line: { style: "solid", fill: C.teal, width: 3 },
  });
  text(slide, code, 122, top + 26, 940, (opts.height ?? 408) - 46, {
    fontFace: "Courier New",
    fontSize: opts.fontSize ?? 19,
    color: C.white,
  });
  return slide;
}

function stepsSlide(title, eyebrow, steps, opts = {}) {
  const slide = contentSlide(title, eyebrow);
  const top = 168;
  const rowH = opts.rowH ?? 70;
  steps.forEach((step, i) => {
    const y = top + i * rowH;
    shape(slide, "ellipse", 80, y + 2, 42, 42, {
      fill: C.teal,
      line: { style: "solid", fill: "none", width: 0 },
    });
    text(slide, String(i + 1), 92, y + 10, 18, 22, {
      fontSize: 18,
      bold: true,
      color: C.white,
      alignment: "center",
    });
    text(slide, step, 144, y, 930, 48, {
      fontSize: opts.fontSize ?? 22,
      color: C.dark,
    });
  });
  return slide;
}

titleSlide(
  "Trabalho Avaliativo",
  "Sistema de Estoque e Vendas com Python",
  "Estrutura de Dados • Valor: 2,0 pontos • Entrega: 11/09/2026 às 23:59"
);

tableSlide("O contrato do trabalho em uma tela", "Informações gerais",
  ["Informação", "Definição"],
  [
    ["Peso", "2,0 pontos na nota da disciplina"],
    ["Grupo", "até 6 integrantes"],
    ["Linguagem", "Python"],
    ["Execução", "terminal"],
    ["Entrega", "AVA, tópico ENTREGAS"],
    ["Repositório", "GitHub obrigatoriamente público"],
    ["Data limite", "11/09/2026 às 23:59"],
  ],
  [330, 700]
);

bulletsSlide("Podem usar os códigos feitos em aula", "Ponto importante",
  [
    "É permitido utilizar, adaptar e evoluir os códigos desenvolvidos em aula.",
    "O grupo deve entender o código usado e integrá-lo corretamente ao sistema.",
    "Referências úteis: aula03/Pilha.py, aula04/Fila.py e aula06/LSE.py.",
    "Códigos de POO das aulas anteriores também podem servir como base.",
    "Copiar sem adaptar ao problema não substitui a implementação do trabalho.",
  ],
  { rowH: 62 }
);

bulletsSlide("O objetivo é integrar os conteúdos em um sistema real", "Objetivo",
  [
    "Desenvolver um Sistema de Estoque e Vendas executado pelo terminal.",
    "Aplicar estruturas de dados no funcionamento do sistema.",
    "Usar POO, algoritmos, persistência e tratamento de erros de forma integrada.",
    "Evitar implementações apenas decorativas ou feitas só para cumprir tabela.",
  ],
  { intro: "O foco da avaliação será a aplicação prática e correta dos conteúdos estudados.", rowH: 70 }
);

bulletsSlide("O sistema deve simular uma pequena loja", "Descrição geral",
  [
    "Cadastrar e gerenciar clientes",
    "Cadastrar e gerenciar produtos",
    "Controlar estoque",
    "Realizar e registrar vendas",
    "Desfazer a última operação",
    "Ordenar produtos e usar Busca Binária",
    "Exibir informações e relatórios",
    "Salvar e carregar dados automaticamente",
  ],
  { cols: 2, rowH: 62 }
);

sectionSlide("Modelagem do sistema", "Primeiro, os objetos principais que representam a loja.", 1);

twoColumnSlide("Cliente e Produto são as entidades básicas", "Classes mínimas",
  "Cliente",
  ["ID único", "Nome obrigatório", "Armazenado na Lista Simplesmente Encadeada"],
  "Produto",
  ["ID único", "Nome obrigatório", "Quantidade disponível", "Preço maior que zero", "Armazenado na Lista Duplamente Encadeada"]
);

bulletsSlide("Venda conecta cliente, produtos e estoque", "Classe Venda",
  [
    "Cada venda possui ID, cliente, produtos vendidos, quantidades e valor total.",
    "Uma venda pode conter um ou mais produtos.",
    "O valor total deve ser calculado automaticamente.",
    "O grupo pode criar atributos ou classes extras se isso melhorar a organização.",
  ],
  { rowH: 76 }
);

tableSlide("Cada estrutura tem uma responsabilidade obrigatória", "Estruturas de dados",
  ["Estrutura", "Aplicação obrigatória"],
  [
    ["LSE", "armazenamento dos clientes"],
    ["LDE", "armazenamento dos produtos"],
    ["Fila", "vendas realizadas na ordem em que aconteceram"],
    ["Pilha", "histórico usado para desfazer operações"],
  ],
  [340, 690]
);

bulletsSlide("As estruturas precisam participar do funcionamento", "Regra importante",
  [
    "Não vale criar uma estrutura apenas para aparecer no código.",
    "A LSE deve ser usada nas operações reais de clientes.",
    "A LDE deve ser usada nas operações reais de produtos.",
    "Fila e Pilha devem afetar diretamente vendas e desfazer.",
    "Listas nativas podem apoiar conversões, mas não substituir as estruturas obrigatórias.",
  ],
  { rowH: 62 }
);

sectionSlide("Menu e funcionalidades", "O menu é o mapa do sistema e deve ser claro para o usuário.", 2);

codeBlockSlide("Exemplo de menu: clientes e produtos", "Menu numérico",
`==============================
 SISTEMA DE ESTOQUE E VENDAS
==============================
1  - Cadastrar cliente
2  - Listar clientes
3  - Buscar cliente
4  - Remover cliente

5  - Cadastrar produto
6  - Listar produtos
7  - Buscar produto
8  - Atualizar estoque
9  - Remover produto
10 - Listar produtos em ordem inversa
11 - Listar produtos ordenados
12 - Buscar produto por ID usando Busca Binária`,
  { fontSize: 17, height: 438 }
);

codeBlockSlide("Exemplo de menu: vendas e relatórios", "Menu numérico",
`13 - Realizar venda
14 - Visualizar fila de vendas
15 - Visualizar primeira venda da fila

16 - Exibir valor total do estoque
17 - Exibir valor total das vendas
18 - Exibir clientes e valores totais gastos
19 - Exibir cliente que mais gastou
20 - Exibir produto mais vendido`,
  { note: "As opções precisam estar acessíveis pelo terminal e validar entradas inválidas.", fontSize: 22, height: 360 }
);

codeBlockSlide("Exemplo de menu: sistema e saída", "Menu numérico",
`21 - Desfazer última operação
0  - Sair

Escolha uma opção: _

Regra:
se a opção for inválida, mostre uma mensagem,
não encerre o programa e volte ao menu principal.`,
  { note: "Não deve existir opção manual para salvar ou carregar dados.", fontSize: 24, height: 330 }
);

bulletsSlide("Clientes ficam na Lista Simplesmente Encadeada", "Gerenciamento de clientes",
  [
    "Cadastrar cliente",
    "Listar clientes",
    "Buscar cliente",
    "Remover cliente",
    "Garantir ID único",
    "Bloquear nomes vazios",
  ],
  { cols: 2, rowH: 70 }
);

bulletsSlide("Produtos ficam na Lista Duplamente Encadeada", "Gerenciamento de produtos",
  [
    "Cadastrar, listar, buscar e remover produto",
    "Atualizar quantidade em estoque",
    "Visualizar do início para o fim",
    "Visualizar do fim para o início",
    "Garantir preço maior que zero",
    "Impedir estoque negativo",
  ],
  { cols: 2, rowH: 70, fontSize: 23 }
);

bulletsSlide("Uma venda só acontece se tudo estiver válido", "Realização de vendas",
  [
    "Cliente precisa estar cadastrado.",
    "Venda deve ter um ou mais produtos.",
    "Todos os produtos informados precisam existir.",
    "Cada quantidade deve ser inteira e maior que zero.",
    "Deve haver estoque suficiente para todos os itens.",
  ],
  { rowH: 66 }
);

flowSlide("Fluxo de venda válida", "Passo a passo",
  ["Validar cliente", "Validar produtos", "Calcular total", "Baixar estoque", "Salvar venda"]
);

flowSlide("Venda inválida não altera dados", "Passo a passo",
  ["Encontrar erro", "Mostrar mensagem", "Cancelar ação", "Preservar dados", "Voltar ao menu"]
);

bulletsSlide("A Fila preserva a ordem das vendas realizadas", "Fila de vendas",
  [
    "A primeira venda realizada permanece como a primeira da estrutura.",
    "A visualização deve respeitar o princípio FIFO.",
    "Ao reiniciar o programa, as vendas devem voltar para a Fila na ordem correta.",
    "O sistema deve tratar tentativa de acessar Fila vazia.",
  ],
  { rowH: 76 }
);

bulletsSlide("A Pilha permite desfazer a última operação", "Pilha e desfazer",
  [
    "A funcionalidade segue o princípio LIFO.",
    "A Pilha deve guardar dados suficientes para restaurar o estado anterior.",
    "Desfazer uma venda devolve todos os produtos ao estoque.",
    "A venda desfeita deixa de fazer parte do histórico correspondente.",
    "Os arquivos devem ser atualizados após o desfazer.",
  ],
  { rowH: 62 }
);

sectionSlide("Algoritmos obrigatórios", "Ordenação manual e Busca Binária precisam aparecer no uso real do sistema.", 3);

bulletsSlide("Cada grupo escolhe um algoritmo de ordenação", "Ordenação",
  [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Apenas um algoritmo precisa ser escolhido e implementado manualmente.",
    "Não é permitido usar sort(), sorted() ou biblioteca equivalente.",
  ],
  { cols: 2, rowH: 70, fontSize: 22 }
);

bulletsSlide("Produtos devem ser ordenados pelo menos por ID", "Ordenação dos produtos",
  [
    "Ordenação por ID é obrigatória.",
    "Ordenação por nome, preço e quantidade é opcional.",
    "A ordenação por ID prepara os dados para a Busca Binária.",
    "A estrutura principal continua sendo a LDE.",
  ],
  { rowH: 76 }
);

flowSlide("A coleção auxiliar existe só para ordenar e buscar", "Coleção auxiliar",
  ["Produtos na LDE", "Criar coleção auxiliar", "Ordenar manualmente", "Usar o resultado", "Manter LDE principal"]
);

flowSlide("Busca Binária localiza produto por ID", "Busca Binária",
  ["Ler produtos da LDE", "Ordenar por ID", "Solicitar ID", "Aplicar Busca Binária", "Mostrar resultado"]
);

bulletsSlide("O que não é permitido em ordenação e busca", "Cuidados obrigatórios",
  [
    "Não usar sort(), sorted() ou bibliotecas para ordenar.",
    "Não aplicar Busca Binária em dados desordenados.",
    "Não usar biblioteca pronta de Busca Binária.",
    "Não trocar a Busca Binária por busca sequencial.",
    "Não substituir a LDE por uma lista auxiliar permanente.",
  ],
  { rowH: 64 }
);

sectionSlide("Persistência e resiliência", "O sistema precisa continuar funcionando e preservar dados.", 4);

bulletsSlide("Os dados devem sobreviver ao encerramento do programa", "Persistência automática",
  [
    "Salvar clientes, produtos e vendas.",
    "Arquivos mínimos esperados: clientes.csv, produtos.csv e vendas.csv.",
    "TXT equivalente é permitido, se guardar todas as informações.",
    "O grupo deve definir como armazenar vendas com múltiplos produtos.",
  ],
  { rowH: 76 }
);

flowSlide("Ao iniciar, o sistema reconstrói as estruturas", "Carregamento",
  ["Abrir arquivos", "Carregar clientes", "Reconstruir LSE", "Reconstruir LDE", "Reconstruir Fila"]
);

flowSlide("Alteração válida salva automaticamente", "Salvamento",
  ["Validar ação", "Alterar memória", "Atualizar estruturas", "Gravar arquivos", "Voltar ao menu"]
);

bulletsSlide("Regra central: o sistema não pode parar por erro previsto", "Tratamento de erros",
  [
    "Toda entrada do terminal deve ser validada antes de ser usada.",
    "Erro previsto não pode encerrar abruptamente a execução.",
    "A ação inválida não deve ser finalizada.",
    "Os dados existentes devem ser preservados.",
    "Depois da mensagem de erro, o sistema deve voltar ao menu.",
  ],
  { rowH: 62 }
);

checklistSlide("O sistema precisa tratar erros previsíveis", "Tratamentos mínimos",
  [
    "opção de menu inválida",
    "letras quando número é esperado",
    "campos obrigatórios vazios",
    "IDs inexistentes ou duplicados",
    "preço inválido",
    "quantidade inválida",
    "estoque insuficiente",
    "cliente ou produto inexistente",
    "remoção de item inexistente",
    "listagens sem registros",
    "Fila ou Pilha vazia",
    "arquivos inexistentes, vazios ou inválidos",
  ]
);

flowSlide("Padrão esperado para qualquer erro", "Erro tratado",
  ["Detectar problema", "Explicar ao usuário", "Cancelar ação", "Não salvar alteração", "Voltar ao menu"]
);

sectionSlide("Organização e trabalho em grupo", "Um projeto legível é mais fácil de testar, explicar e corrigir.", 5);

codeBlockSlide("Árvore sugerida de arquivos e pastas", "Organização",
`projeto/
├── main.py
├── models/
│   ├── cliente.py
│   ├── produto.py
│   └── venda.py
├── estruturas/
│   ├── nodo.py
│   ├── lse.py
│   ├── lde.py
│   ├── fila.py
│   └── pilha.py
├── algoritmos/
│   ├── ordenacao.py
│   └── busca_binaria.py
├── services/
│   ├── estoque_service.py
│   └── persistencia_service.py
├── data/
│   ├── clientes.csv
│   ├── produtos.csv
│   └── vendas.csv
└── README.md`,
  { fontSize: 14, height: 458 }
);

bulletsSlide("A árvore é sugestão, não limite", "Organização",
  [
    "O grupo pode criar mais classes, arquivos e pastas se precisar.",
    "O importante é separar responsabilidades com clareza.",
    "Evitem concentrar tudo em um único main.py.",
    "Serviços podem ajudar a organizar regras de venda, estoque e persistência.",
    "Cada integrante deve compreender a estrutura adotada pelo grupo.",
  ],
  { rowH: 62 }
);

stepsSlide("Um caminho seguro para desenvolver", "Passo a passo sugerido",
  [
    "Criem as classes Cliente, Produto e Venda.",
    "Implementem LSE, LDE, Fila e Pilha usando os códigos de aula como base.",
    "Montem o menu com entradas validadas desde o início.",
    "Implementem clientes e produtos antes de vendas.",
    "Só depois integrem venda, desfazer, ordenação, busca e persistência.",
    "Testem uma funcionalidade por vez antes de continuar.",
  ],
  { rowH: 68, fontSize: 21 }
);

stepsSlide("Como testar durante o desenvolvimento", "Roteiro prático",
  [
    "Comecem sempre com arquivos vazios ou inexistentes.",
    "Cadastrem clientes e produtos válidos.",
    "Tentem entradas inválidas em cada campo.",
    "Realizem uma venda válida e confiram estoque, Fila e arquivo.",
    "Tentem venda inválida e confiram que nada mudou.",
    "Reiniciem o programa e verifiquem se os dados carregam corretamente.",
  ],
  { rowH: 68, fontSize: 21 }
);

checklistSlide("Cenários mínimos de teste manual", "Testes",
  [
    "ID duplicado de cliente",
    "ID duplicado de produto",
    "preço zero ou negativo",
    "quantidade negativa",
    "venda sem estoque suficiente",
    "venda com produto inexistente",
    "desfazer sem operações",
    "listar Fila vazia",
    "arquivo CSV vazio",
    "arquivo CSV com dado inválido",
    "Busca Binária por ID existente",
    "Busca Binária por ID inexistente",
  ]
);

bulletsSlide("O README mostra que o grupo entende o sistema", "README e complexidade",
  [
    "Identificação da disciplina, trabalho e integrantes.",
    "Descrição do sistema e instruções de execução.",
    "Estrutura de diretórios do projeto.",
    "Explicação da LSE, LDE, Fila e Pilha no sistema.",
    "Algoritmo de ordenação escolhido, Busca Binária e persistência.",
    "Complexidade do algoritmo de ordenação e da Busca Binária.",
  ],
  { rowH: 58, fontSize: 22 }
);

tableSlide("Entrega, participação e avaliação fecham o trabalho", "Avaliação",
  ["Critério", "Valor"],
  [
    ["LSE e LDE", "0,30"],
    ["Fila e Pilha", "0,30"],
    ["Aplicação correta das estruturas", "0,20"],
    ["Algoritmo de ordenação", "0,20"],
    ["Busca Binária", "0,20"],
    ["POO e organização", "0,25"],
    ["Funcionalidades obrigatórias", "0,20"],
    ["Persistência automática", "0,15"],
    ["Erros, Git, README e participação", "0,20"],
  ],
  [760, 170]
);

checklistSlide("Antes de finalizar, confiram tudo", "Checklist final",
  [
    "postagem no tópico ENTREGAS do AVA",
    "nomes de todos os integrantes",
    "link correto do GitHub",
    "repositório público",
    "código completo disponível",
    "README.md disponível",
    "arquivos de persistência incluídos",
    "programa executando corretamente",
    "entrega até 11/09/2026 às 23:59",
    "uma única postagem por grupo",
    "todos fizeram commits reais",
    "todos entendem o sistema entregue",
  ]
);

async function writeBlob(path, blob) {
  await fs.writeFile(path, new Uint8Array(await blob.arrayBuffer()));
}

async function main() {
  await fs.mkdir(`${BUILD}/rendered-43`, { recursive: true });
  for (const [index, slide] of pres.slides.items.entries()) {
    const png = await pres.export({ slide, format: "png", scale: 1 });
    await writeBlob(`${BUILD}/rendered-43/slide-${String(index + 1).padStart(2, "0")}.png`, png);
  }
  const montage = await pres.export({ format: "webp", montage: true, scale: 1 });
  await writeBlob(`${BUILD}/montage.webp`, montage);
  const pptx = await PresentationFile.exportPptx(pres);
  await pptx.save(OUT);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
