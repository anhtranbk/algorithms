public class CountPrimes {

    public int countPrimes(int n) {
        int count = 0;
        boolean[] primes = new boolean[n];
        for (int i = 2; i < n; i++) {
            primes[i] = true;
        }
        for (int i = 2; i*i < n; i++) {
            if (!primes[i]) continue;
            int t = i*i;
            while (t < n) {
                primes[t] = false;
                t += i;
            }
        }
        for (int i = 2; i < n; i++) {
            if (primes[i]) count += 1;
        }
        return count;
    }

    private boolean isPrime(int num) {
        if (num <= 1) return false;
        // Loop's ending condition is i * i <= num instead of i <= sqrt(num)
        // to avoid repeatedly calling an expensive function sqrt().
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        CountPrimes cp = new CountPrimes();
        int ret = cp.countPrimes(10);
        System.out.println(ret);
    }
}
