from langchain_core.documents import Document


class Loader:
    @staticmethod
    def load():
        documents = [
            Document(page_content="Devsloop is a software development firm based in Gujranwala, Pakistan, with a team "
                                  "of 20 employees. The company is led by CEO Ammad Javaid, with Shehwar Khalid as a "
                                  "partner. Devsloop has managed Adly clients and has worked on notable projects such "
                                  "as Beambox, Rapid Translate, Pageflows, Upcall, and Easylama"),
            Document(page_content="It has an HR manager named Emama Babur, and salaries are disbursed on the 1st of "
                                  "each month. Devsloop provide a machine either MAC or Laptop to all employees"),
            Document(page_content="My name is Salman Ahmad. I am learning Data Science. I joined the company in "
                                  "september 2023. I did Graduation from Gift University")
        ]
        return documents
