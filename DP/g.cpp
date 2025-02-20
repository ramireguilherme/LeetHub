#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int tests;
    cin >> tests;

    while (tests--) {
        int n_weights;
        cin >> n_weights;

        vector<int> weights(n_weights);
        vector<int> values(n_weights);
        
        for (int i = 0; i < n_weights; ++i) {
            cin >> values[i] >> weights[i];
        }

        int n = values.size();

        int people;
        cin >> people;

        vector<int> max_weights(people);

        for (int i = 0; i < people; ++i) {
            cin >> max_weights[i];
        }

        int max_max_weight = *max_element(max_weights.begin(), max_weights.end());

        vector<vector<int>> dp(n + 1, vector<int>(max_max_weight + 1, 0));

        for (int i = 1; i <= n; ++i) {
            for (int w = 0; w <= max_max_weight; ++w) {
                if (weights[i - 1] <= w) {
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        int result = 0;
        for (int weight : max_weights) {
            result += dp[n][weight];
        }

        cout << result << endl;
    }

    return 0;
}
