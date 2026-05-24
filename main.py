from recurrence import RecurrenceSolver

solver = RecurrenceSolver(
    coefficients=[1, -5, 6],
    initial_conditions={0:1, 1:4}
)

solver.solve()
solver.show_steps()

def main():

    if __name__ == "__main__":
        main()