# %% [markdown]
# **Task 08: Completing missing data**

# %%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

# %% [markdown]
# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# %% [markdown]
# **Importamos las librerias**

# %%
from rdflib.namespace import RDF
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://data.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# %% [markdown]
# *Listamos todos los elementos de la clase Person*

# %%
for s, p, o in g1.triples((None, RDF.type, ns.Person)):
    print(s)

# %% [markdown]
# *Seleccionamos solo los campos de name, family name y emaul, para añadirlos al primero. Usare SPARQL.*

# %%
q = prepareQuery("""select ?s ?p ?o where { ?s ?p ?o. filter(?p=vcard:FN || ?p=vcard:Given || ?p=vcard:EMAIL) }""", initNs={"vcard": vcard})
for newData in g2.query(q):
    g1.add(newData)

# %% [markdown]
# *Finalmente visualizamos el resultado*

# %%
for s, p, o in g1:
    print(s, p, o)


