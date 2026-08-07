from app.loaders.curriculum_loader import CurriculumLoader

loader = CurriculumLoader()

curriculum = loader.load()

print(curriculum)