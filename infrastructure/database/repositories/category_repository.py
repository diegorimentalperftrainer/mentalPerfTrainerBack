from infrastructure.database.models.category import Category

class CategoryRepository():

    @staticmethod
    def get_categories():
        return Category.query.all()