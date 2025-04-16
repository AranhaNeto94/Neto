🌳 Classificação de Segmento Empresarial com Árvore de Decisão
Este projeto utiliza o algoritmo de árvore de decisão para classificar empresas em diferentes segmentos com base em variáveis como receita anual, número de funcionários e localização.

🧪 Tecnologias usadas
Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-learn

🔍 Etapas do projeto
Análise exploratória dos dados (EDA): Estudo inicial para entender a distribuição das variáveis e relações com o segmento.

Pré-processamento: Conversão de colunas categóricas com LabelEncoder, verificação de valores nulos e preparação dos dados para o modelo.

Divisão em treino e teste: Separação dos dados com train_test_split e definição das variáveis X (features) e y (target).

Criação e treinamento do modelo: Implementação de um modelo de Árvore de Decisão com DecisionTreeClassifier.

Avaliação de desempenho: Cálculo da acurácia com validação cruzada e exibição da matriz de confusão.

Visualização da árvore: Geração do gráfico da árvore de decisão com plot_tree, mostrando os critérios de divisão das classes.

📌 Conclusão
O modelo obteve bom desempenho na classificação dos segmentos empresariais, apresentando acurácia consistente nos testes realizados. A árvore de decisão oferece interpretabilidade, facilitando a análise das regras de classificação.

📁 Dataset
Arquivo CSV incluído na pasta dataset/.
