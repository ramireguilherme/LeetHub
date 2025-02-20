#include <iostream>

int main() {
    bool sol = false;
    int x, y, z;
    int A = 0;
    int B = 0;
    int C = 0; 
    int tests;
    
    std::cin >> tests;
    
    for (int i = 0; i < tests; i++) {
        std::cin >> A >> B >> C;
        sol = false;
        for (x = -21; x <= 21 && !sol; x++) {
            if (x * x <= C) {
                for (y = x + 1; y <= 100 && !sol; y++) {
                    if (x * x + y * y <= C) {
                        for (z = y + 1; z <= 100 && !sol; z++) {
                            if (x + y + z == A && x * y * z == B && x * x + y * y + z * z == C) {
                                std::cout << x << " " << y << " " << z << std::endl;
                                sol = true;
                                break;
                            }
                        }
                    if (sol)
                    {
                        break;
                    }
                    
                    }
                }
                if (sol)
                {
                    break;
                }
                
            }
        }

        if (!sol) {
            std::cout << "No solution." << std::endl;
        }
    }

    return 0;
}
