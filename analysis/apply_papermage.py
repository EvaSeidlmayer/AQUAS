from papermage.recipes import CoreRecipe

recipe = CoreRecipe()
doc = recipe.run("/home/ruth/Documents/Literatur/papermage.pdf")
#print(doc.metadata)
for page in doc.pages:
    print(f'\n=== PAGE: {page.id} ===\n\n')
    for row in page.rows:
        print(row.text)


# benjamin tipp: .text()