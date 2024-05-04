import cleanText

##text es un corpus, que contiene informacion variada sobre muchos temas(bag of words) que necesitamos conseguir(estoy en eso)

def createMatrix(text):
    wordsText = cleanText.cleanText(text)
    matrix = {}
    for i in range(len(wordsText)):
        matrix[wordsText[i]] = {}
        for j in range(len(wordsText)):
            if wordsText[j] not in matrix[wordsText[i]]:
                matrix[wordsText[i]][wordsText[j]] = calculateFrequency(wordsText[i], wordsText[j], wordsText)
            else:
                matrix[wordsText[i]][wordsText[j]] += calculateFrequency(wordsText[i], wordsText[j], wordsText)
    return matrix

def calculateFrequency(word1, word2, wordsText):
    count = 0
    for i in range(len(wordsText)-1):
        if wordsText[i] == word1 and (wordsText[i+1] == word2 or wordsText[i-1] == word2):
            count += 1
    return count

def vectorizeWord(word,matrix):
    importantWords = {}
    word = cleanText.parseSemantic(word)
    word = cleanText.purgeFillers(word)
    vector = []
    for key in matrix[word]:
        vector.append(matrix[word][key])
        if matrix[word][key] > 1:
            importantWords[key] = matrix[word][key]
    
    #Ordenamos las palabras por importancia
    sortedImportantWords = sorted(importantWords.items(), key=lambda x: x[1], reverse=True)

    if vector == []:
        return [1] * len(matrix)
    return vector, sortedImportantWords

##Necesitamos un texto lo suficientemente bueno, que hable de muchos temas para poder abordar casi todos los temas de los que se nos hable, es lo que el 
##Jorch nos dijo que seria nuestra bag of words, que se usa para vectorizar las palabras y posteriormente compararlas



'''Estaba probando un par'''

text = 'La Inteligencia Artificial (IA) ha emergido como una fuerza poderosa que está remodelando fundamentalmente la forma en que interactuamos, trabajamos y vivimos en la sociedad moderna. Con avances rápidos y continuos en el campo de la informática, la IA está demostrando ser una herramienta versátil con aplicaciones en una amplia gama de industrias, desde la atención médica hasta la agricultura, desde la manufactura hasta la educación. Su creciente influencia promete mejorar la eficiencia, la productividad y la calidad de vida en todo el mundo. Una de las áreas más impactadas por la IA es la economía. Con algoritmos sofisticados y sistemas de aprendizaje automático, las empresas pueden optimizar sus operaciones, mejorar la toma de decisiones y anticipar las tendencias del mercado. Esto se traduce en una mayor competitividad y rentabilidad, así como en la creación de nuevos modelos de negocio. Sin embargo, también plantea desafíos, como la automatización de trabajos tradicionales y la necesidad de reentrenamiento de la fuerza laboral para adaptarse a un entorno cambiante. En el ámbito de la atención médica, la IA está revolucionando la forma en que se diagnostican y tratan las enfermedades. Desde la detección temprana del cáncer hasta la personalización de los tratamientos, los sistemas de IA están mejorando la precisión y la eficacia de la atención médica, salvando vidas en el proceso. Además, la IA está siendo utilizada para gestionar grandes cantidades de datos de salud, lo que permite a los profesionales sanitarios tomar decisiones informadas y predecir brotes de enfermedades con mayor precisión. La IA también está desempeñando un papel importante en la conservación del medio ambiente y la gestión de recursos naturales. Los algoritmos de IA pueden analizar datos ambientales a gran escala y ayudar a identificar patrones y tendencias que de otra manera serían difíciles de detectar. Esto permite una mejor planificación y gestión de recursos, así como la implementación de políticas más efectivas para abordar los desafíos ambientales globales, como el cambio climático y la pérdida de biodiversidad. En el ámbito de la educación, la IA está transformando la forma en que se enseña y se aprende. Los sistemas de tutoría inteligente pueden adaptarse al ritmo y al estilo de aprendizaje de cada estudiante, proporcionando una experiencia educativa personalizada y mejorando la retención del conocimiento. Además, la IA está siendo utilizada para desarrollar herramientas de evaluación más sofisticadas, que pueden medir no solo el conocimiento factual, sino también las habilidades cognitivas y socioemocionales. Sin embargo, el crecimiento y la implementación de la IA también plantean una serie de preocupaciones éticas y sociales. El sesgo algorítmico, por ejemplo, puede perpetuar y amplificar las desigualdades existentes, mientras que la falta de transparencia en los sistemas de IA puede socavar la confianza del público y dificultar la rendición de cuentas. Además, existe la preocupación de que la IA pueda ser utilizada para propósitos maliciosos, como la vigilancia masiva o la manipulación de la información. Para abordar estos desafíos, es crucial un enfoque ético y colaborativo para el desarrollo y la implementación de la IA. Esto incluye la incorporación de principios éticos en el diseño de algoritmos, la promoción de la diversidad y la inclusión en la comunidad de IA, y la creación de marcos regulatorios sólidos que protejan los derechos y las libertades de los individuos. Además, es importante fomentar la alfabetización digital y la educación en IA en todos los niveles de la sociedad, para garantizar que las personas comprendan los impactos y las implicaciones de esta tecnología en sus vidas. En última instancia, la IA tiene el potencial de mejorar significativamente nuestra calidad de vida y abordar algunos de los desafíos más apremiantes de nuestro tiempo. Sin embargo, su éxito dependerá en gran medida de cómo elijamos utilizar y regular esta tecnología emergente. Con un enfoque cuidadoso y colaborativo, podemos aprovechar todo el potencial de la IA para construir un futuro más justo, equitativo y sostenible para todos.'
#wordsText = cleanText.cleanText(text)

matrix = createMatrix(text)

vector, importantWords  = vectorizeWord('ia',matrix)

#print(vector)
print(importantWords)

