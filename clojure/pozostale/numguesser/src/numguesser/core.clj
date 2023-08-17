(ns numguesser.core
  (:gen-class))


(defn log2 [n]
  (/ (Math/log n) (Math/log 2)))


(let [maxnumber (Integer/parseInt (read-line))]
  (def number (rand-int maxnumber))
  (def start_attempts (int (Math/ceil (log2 maxnumber)))))


(defn guesser [attempts]
  (if (= attempts 0)
    (println "You lose, you lose again! Number was: " number)
    (let [guess (Integer/parseInt (read-line))]
      (if (= guess number)
        (println "You win!")
        (do
          (if (> guess number)
            (println "Too big!")
            (println "Too small!"))
          (recur (- attempts 1)))))))


(defn -main []
  (guesser start_attempts))
