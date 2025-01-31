from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question

class Command(BaseCommand):
    help = 'Creates initial quizzes for ChemQuest'

    def handle(self, *args, **kwargs):
        # Create Basic Concepts Quiz 1
        basic_quiz1 = Quiz.objects.create(
            title="Introduction to Chemistry Basics - Quiz 1",
            description="Test your knowledge of fundamental chemistry concepts including matter, elements, and compounds.",
            chapter="basic",
            time_limit=30
        )

        # Questions for Basic Concepts Quiz 1
        basic_quiz1_questions = [
            {
                "text": "What is the smallest unit of matter that retains all properties of an element?",
                "option1": "Atom",
                "option2": "Molecule",
                "option3": "Compound",
                "option4": "Mixture",
                "correct_answer": "Atom"
            },
            {
                "text": "Which state of matter has a definite volume but no definite shape?",
                "option1": "Solid",
                "option2": "Liquid",
                "option3": "Gas",
                "option4": "Plasma",
                "correct_answer": "Liquid"
            },
            {
                "text": "What is the SI unit for temperature?",
                "option1": "Fahrenheit",
                "option2": "Celsius",
                "option3": "Kelvin",
                "option4": "Rankine",
                "correct_answer": "Kelvin"
            },
            {
                "text": "Which of these is a homogeneous mixture?",
                "option1": "Pizza",
                "option2": "Salt water",
                "option3": "Granite",
                "option4": "Sand and water",
                "correct_answer": "Salt water"
            },
            {
                "text": "What is the process of a solid changing directly to a gas called?",
                "option1": "Melting",
                "option2": "Sublimation",
                "option3": "Condensation",
                "option4": "Evaporation",
                "correct_answer": "Sublimation"
            },
            {
                "text": "Which of these represents a chemical change?",
                "option1": "Ice melting",
                "option2": "Paper burning",
                "option3": "Sugar dissolving",
                "option4": "Water evaporating",
                "correct_answer": "Paper burning"
            },
            {
                "text": "What is the law that states matter cannot be created or destroyed?",
                "option1": "Law of Conservation of Mass",
                "option2": "Law of Definite Proportions",
                "option3": "Law of Multiple Proportions",
                "option4": "Law of Conservation of Energy",
                "correct_answer": "Law of Conservation of Mass"
            },
            {
                "text": "Which of these is an intensive property?",
                "option1": "Mass",
                "option2": "Volume",
                "option3": "Density",
                "option4": "Weight",
                "correct_answer": "Density"
            },
            {
                "text": "What type of mixture can be separated by filtration?",
                "option1": "Salt water",
                "option2": "Air",
                "option3": "Sand and water",
                "option4": "Alcohol and water",
                "correct_answer": "Sand and water"
            },
            {
                "text": "Which of these is a pure substance?",
                "option1": "Air",
                "option2": "Bronze",
                "option3": "Diamond",
                "option4": "Milk",
                "correct_answer": "Diamond"
            }
        ]

        # Create Basic Concepts Quiz 2
        basic_quiz2 = Quiz.objects.create(
            title="Chemical Laws and Theories - Quiz 2",
            description="Test your understanding of fundamental chemical laws and theories.",
            chapter="basic",
            time_limit=30
        )

        # Questions for Basic Concepts Quiz 2
        basic_quiz2_questions = [
            {
                "text": "Who proposed the law of conservation of mass?",
                "option1": "Dalton",
                "option2": "Lavoisier",
                "option3": "Proust",
                "option4": "Mendeleev",
                "correct_answer": "Lavoisier"
            },
            {
                "text": "What is the law of definite proportions also known as?",
                "option1": "Law of Conservation of Mass",
                "option2": "Law of Multiple Proportions",
                "option3": "Law of Constant Composition",
                "option4": "Law of Combining Volumes",
                "correct_answer": "Law of Constant Composition"
            },
            {
                "text": "Which law states that gases combine in simple whole number ratios?",
                "option1": "Gay-Lussac's Law",
                "option2": "Charles's Law",
                "option3": "Boyle's Law",
                "option4": "Avogadro's Law",
                "correct_answer": "Gay-Lussac's Law"
            },
            {
                "text": "What does Avogadro's number represent?",
                "option1": "Number of atoms in 1g of hydrogen",
                "option2": "Number of molecules in 22.4L of gas",
                "option3": "Number of particles in one mole",
                "option4": "Number of neutrons in an atom",
                "correct_answer": "Number of particles in one mole"
            },
            {
                "text": "Which scientist proposed the first atomic theory?",
                "option1": "Thomson",
                "option2": "Rutherford",
                "option3": "Dalton",
                "option4": "Bohr",
                "correct_answer": "Dalton"
            },
            {
                "text": "What is the value of Avogadro's number?",
                "option1": "6.022 × 10²²",
                "option2": "6.022 × 10²³",
                "option3": "6.022 × 10²⁴",
                "option4": "6.022 × 10²⁵",
                "correct_answer": "6.022 × 10²³"
            },
            {
                "text": "Which law relates the volume and pressure of a gas?",
                "option1": "Charles's Law",
                "option2": "Boyle's Law",
                "option3": "Gay-Lussac's Law",
                "option4": "Graham's Law",
                "correct_answer": "Boyle's Law"
            },
            {
                "text": "What is the SI unit for amount of substance?",
                "option1": "Gram",
                "option2": "Kilogram",
                "option3": "Mole",
                "option4": "Molecule",
                "correct_answer": "Mole"
            },
            {
                "text": "Which law states that the total pressure of a mixture of gases equals the sum of partial pressures?",
                "option1": "Charles's Law",
                "option2": "Boyle's Law",
                "option3": "Dalton's Law",
                "option4": "Graham's Law",
                "correct_answer": "Dalton's Law"
            },
            {
                "text": "What is the standard temperature in Kelvin?",
                "option1": "0 K",
                "option2": "273 K",
                "option3": "298 K",
                "option4": "373 K",
                "correct_answer": "273 K"
            }
        ]

        # Create Redox Quiz 1
        redox_quiz1 = Quiz.objects.create(
            title="Oxidation and Reduction Fundamentals - Quiz 1",
            description="Test your understanding of oxidation, reduction, and electron transfer.",
            chapter="redox",
            time_limit=30
        )

        # Questions for Redox Quiz 1
        redox_quiz1_questions = [
            {
                "text": "What is oxidation in terms of electron transfer?",
                "option1": "Gain of electrons",
                "option2": "Loss of electrons",
                "option3": "Gain of protons",
                "option4": "Loss of protons",
                "correct_answer": "Loss of electrons"
            },
            {
                "text": "In a redox reaction, what happens to the reducing agent?",
                "option1": "It is reduced",
                "option2": "It is oxidized",
                "option3": "It remains unchanged",
                "option4": "It disappears",
                "correct_answer": "It is oxidized"
            },
            {
                "text": "What is the oxidation number of oxygen in most compounds?",
                "option1": "+2",
                "option2": "-2",
                "option3": "0",
                "option4": "+1",
                "correct_answer": "-2"
            },
            {
                "text": "What is the oxidation state of hydrogen in most compounds?",
                "option1": "+1",
                "option2": "-1",
                "option3": "0",
                "option4": "+2",
                "correct_answer": "+1"
            },
            {
                "text": "In the reaction Zn + Cu²⁺ → Zn²⁺ + Cu, what is reduced?",
                "option1": "Zn",
                "option2": "Cu²⁺",
                "option3": "Zn²⁺",
                "option4": "Cu",
                "correct_answer": "Cu²⁺"
            },
            {
                "text": "What is the oxidation number of sulfur in H₂SO₄?",
                "option1": "+4",
                "option2": "+6",
                "option3": "-2",
                "option4": "+2",
                "correct_answer": "+6"
            },
            {
                "text": "Which process involves the loss of hydrogen?",
                "option1": "Reduction",
                "option2": "Oxidation",
                "option3": "Hydration",
                "option4": "Hydrogenation",
                "correct_answer": "Oxidation"
            },
            {
                "text": "What is the oxidation number of chromium in K₂Cr₂O₇?",
                "option1": "+3",
                "option2": "+6",
                "option3": "+4",
                "option4": "+5",
                "correct_answer": "+6"
            },
            {
                "text": "In which compound does nitrogen have the highest oxidation state?",
                "option1": "NH₃",
                "option2": "NO",
                "option3": "HNO₃",
                "option4": "N₂",
                "correct_answer": "HNO₃"
            },
            {
                "text": "What type of reaction is Fe + CuSO₄ → FeSO₄ + Cu?",
                "option1": "Decomposition",
                "option2": "Single displacement",
                "option3": "Double displacement",
                "option4": "Synthesis",
                "correct_answer": "Single displacement"
            }
        ]

        # Create Redox Quiz 2
        redox_quiz2 = Quiz.objects.create(
            title="Balancing Redox Equations - Quiz 2",
            description="Practice balancing complex redox equations and identifying redox reactions.",
            chapter="redox",
            time_limit=30
        )

        # Questions for Redox Quiz 2
        redox_quiz2_questions = [
            {
                "text": "In acidic medium, what is added to balance H atoms?",
                "option1": "H⁺",
                "option2": "OH⁻",
                "option3": "H₂O",
                "option4": "O₂",
                "correct_answer": "H⁺"
            },
            {
                "text": "What is the first step in balancing redox equations?",
                "option1": "Balance oxygen atoms",
                "option2": "Balance hydrogen atoms",
                "option3": "Write half-reactions",
                "option4": "Add electrons",
                "correct_answer": "Write half-reactions"
            },
            {
                "text": "In basic medium, what species is used to balance H⁺ ions?",
                "option1": "H⁺",
                "option2": "OH⁻",
                "option3": "H₂O",
                "option4": "O₂",
                "correct_answer": "OH⁻"
            },
            {
                "text": "What must be equal in both half-reactions?",
                "option1": "Number of atoms",
                "option2": "Number of electrons",
                "option3": "Charges",
                "option4": "Coefficients",
                "correct_answer": "Number of electrons"
            },
            {
                "text": "Which ion is commonly reduced in acidic solutions?",
                "option1": "H⁺",
                "option2": "OH⁻",
                "option3": "H₂O",
                "option4": "O₂",
                "correct_answer": "H⁺"
            },
            {
                "text": "In the reaction MnO₄⁻ + C₂O₄²⁻ → Mn²⁺ + CO₂, what is reduced?",
                "option1": "C₂O₄²⁻",
                "option2": "MnO₄⁻",
                "option3": "Mn²⁺",
                "option4": "CO₂",
                "correct_answer": "MnO₄⁻"
            },
            {
                "text": "What is the charge of the permanganate ion (MnO₄⁻)?",
                "option1": "-1",
                "option2": "-2",
                "option3": "+1",
                "option4": "+2",
                "correct_answer": "-1"
            },
            {
                "text": "How many electrons are transferred in Fe³⁺ → Fe²⁺?",
                "option1": "1",
                "option2": "2",
                "option3": "3",
                "option4": "4",
                "correct_answer": "1"
            },
            {
                "text": "What is the oxidation state of Cr in Cr₂O₇²⁻?",
                "option1": "+3",
                "option2": "+6",
                "option3": "+4",
                "option4": "+5",
                "correct_answer": "+6"
            },
            {
                "text": "In which medium does MnO₄⁻ typically reduce to Mn²⁺?",
                "option1": "Basic",
                "option2": "Acidic",
                "option3": "Neutral",
                "option4": "Any medium",
                "correct_answer": "Acidic"
            }
        ]

        # Create Atomic Structure Quiz 1
        atom_quiz1 = Quiz.objects.create(
            title="Atomic Models and Theories - Quiz 1",
            description="Test your knowledge of atomic models and theoretical development.",
            chapter="atom",
            time_limit=30
        )

        # Questions for Atomic Structure Quiz 1
        atom_quiz1_questions = [
            {
                "text": "Who discovered the electron?",
                "option1": "Thomson",
                "option2": "Rutherford",
                "option3": "Bohr",
                "option4": "Dalton",
                "correct_answer": "Thomson"
            },
            {
                "text": "What was Rutherford's gold foil experiment's major finding?",
                "option1": "Electrons exist",
                "option2": "Atoms have a dense nucleus",
                "option3": "Protons exist",
                "option4": "Neutrons exist",
                "correct_answer": "Atoms have a dense nucleus"
            },
            {
                "text": "Which particle has no charge?",
                "option1": "Proton",
                "option2": "Electron",
                "option3": "Neutron",
                "option4": "Positron",
                "correct_answer": "Neutron"
            },
            {
                "text": "What is the charge of a proton?",
                "option1": "-1",
                "option2": "+1",
                "option3": "0",
                "option4": "+2",
                "correct_answer": "+1"
            },
            {
                "text": "Who proposed the planetary model of the atom?",
                "option1": "Thomson",
                "option2": "Rutherford",
                "option3": "Bohr",
                "option4": "Dalton",
                "correct_answer": "Rutherford"
            },
            {
                "text": "What did J.J. Thomson's model of the atom look like?",
                "option1": "Solar system",
                "option2": "Plum pudding",
                "option3": "Solid sphere",
                "option4": "Nuclear model",
                "correct_answer": "Plum pudding"
            },
            {
                "text": "Who discovered the nucleus?",
                "option1": "Thomson",
                "option2": "Rutherford",
                "option3": "Bohr",
                "option4": "Dalton",
                "correct_answer": "Rutherford"
            },
            {
                "text": "What is the mass of an electron relative to a proton?",
                "option1": "1/1836",
                "option2": "1/1000",
                "option3": "1/100",
                "option4": "1/10",
                "correct_answer": "1/1836"
            },
            {
                "text": "Which scientist discovered the neutron?",
                "option1": "Chadwick",
                "option2": "Rutherford",
                "option3": "Bohr",
                "option4": "Thomson",
                "correct_answer": "Chadwick"
            },
            {
                "text": "What year was the neutron discovered?",
                "option1": "1897",
                "option2": "1911",
                "option3": "1932",
                "option4": "1913",
                "correct_answer": "1932"
            }
        ]

        # Create Atomic Structure Quiz 2
        atom_quiz2 = Quiz.objects.create(
            title="Electronic Configuration - Quiz 2",
            description="Test your understanding of electron arrangements and orbital theory.",
            chapter="atom",
            time_limit=30
        )

        # Questions for Atomic Structure Quiz 2
        atom_quiz2_questions = [
            {
                "text": "What is the maximum number of electrons in the first shell?",
                "option1": "2",
                "option2": "8",
                "option3": "18",
                "option4": "32",
                "correct_answer": "2"
            },
            {
                "text": "Which subshell is filled after 3p?",
                "option1": "3d",
                "option2": "4s",
                "option3": "4p",
                "option4": "4d",
                "correct_answer": "4s"
            },
            {
                "text": "What is the electron configuration of Na⁺?",
                "option1": "1s²2s²2p⁶3s¹",
                "option2": "1s²2s²2p⁶",
                "option3": "1s²2s²2p⁶3s²",
                "option4": "1s²2s²2p⁵",
                "correct_answer": "1s²2s²2p⁶"
            },
            {
                "text": "How many orbitals are in the p subshell?",
                "option1": "1",
                "option2": "3",
                "option3": "5",
                "option4": "7",
                "correct_answer": "3"
            },
            {
                "text": "What is the maximum number of electrons in a d orbital?",
                "option1": "2",
                "option2": "6",
                "option3": "10",
                "option4": "14",
                "correct_answer": "2"
            },
            {
                "text": "Which principle states no two electrons can have all four quantum numbers the same?",
                "option1": "Aufbau Principle",
                "option2": "Hund's Rule",
                "option3": "Pauli Exclusion Principle",
                "option4": "Heisenberg Principle",
                "correct_answer": "Pauli Exclusion Principle"
            },
            {
                "text": "What is the electron configuration of Fe²⁺?",
                "option1": "[Ar]3d⁶4s²",
                "option2": "[Ar]3d⁶",
                "option3": "[Ar]3d⁵4s¹",
                "option4": "[Ar]3d⁴4s²",
                "correct_answer": "[Ar]3d⁶"
            },
            {
                "text": "How many electrons can the third shell hold maximum?",
                "option1": "8",
                "option2": "18",
                "option3": "32",
                "option4": "50",
                "correct_answer": "18"
            },
            {
                "text": "What type of orbital has a dumbbell shape?",
                "option1": "s",
                "option2": "p",
                "option3": "d",
                "option4": "f",
                "correct_answer": "p"
            },
            {
                "text": "According to Hund's rule, electrons in orbitals of equal energy will:",
                "option1": "Pair up first",
                "option2": "Remain unpaired with parallel spins",
                "option3": "Remain unpaired with opposite spins",
                "option4": "Share orbitals randomly",
                "correct_answer": "Remain unpaired with parallel spins"
            }
        ]

        # Create all questions for each quiz
        quiz_questions = {
            basic_quiz1: basic_quiz1_questions,
            basic_quiz2: basic_quiz2_questions,
            redox_quiz1: redox_quiz1_questions,
            redox_quiz2: redox_quiz2_questions,
            atom_quiz1: atom_quiz1_questions,
            atom_quiz2: atom_quiz2_questions
        }

        # Create questions for all quizzes
        for quiz, questions in quiz_questions.items():
            for q in questions:
                Question.objects.create(
                    quiz=quiz,
                    text=q["text"],
                    option1=q["option1"],
                    option2=q["option2"],
                    option3=q["option3"],
                    option4=q["option4"],
                    correct_answer=q["correct_answer"]
                )

        self.stdout.write(self.style.SUCCESS('Successfully created all quizzes with questions')) 