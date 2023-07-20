import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, select
from sqlalchemy.orm import registry, relationship, Session

engine = create_engine('mysql+mysqlconnector://root:18222222@localhost:3306/python_db', echo=True)

mapper_registry = registry()
#mapper_registry.metadata

Base = mapper_registry.generate_base()

#Creating the models 
class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title='{0}, description='{1}')>".format(
            self.title, self.description)
  
class Tasks(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)
    
#connect with my database
Base.metadata.create_all(engine)

#create a session with the engine (how we create transactions: transactions are querys)

# with Session(engine) as session:
#     organize_close_project = Project(title='Organize closet',
#             description='Organize closet by color and style')
    
#     session.add(organize_close_project)

#     session.flush()

#     tasks = [
#         Tasks(project_id=organize_close_project.project_id,
#               description= 'Decide what clothes to donate'),
#         Tasks(project_id=organize_close_project.project_id,
#               description='Organize summer clothes'),
#         Tasks(project_id=organize_close_project.project_id,
#               description='Organize winter clothes')
#       ]
# session.bulk_save_objects(tasks)

# session.commit()


#retrieving data

with Session(engine) as session:
    smt = select(Project).where(Project.title == 'Organize closet')
    results = session.execute(smt)
    organize_close_project = results.scalar()

    smt = select(Tasks). where(Tasks.project_id == organize_close_project.project_id)
    results = session.execute(smt)
    for task in results:
        print(task)
