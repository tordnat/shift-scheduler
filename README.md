# Tips fra Magnus Lie Hetland


Hei, hei!

Selv om du har planer om å bruke en lokal søkealgoritme, så vil jeg anbefale deg å vurdere et alternativ først: Å begynne med å sette deg inn i lineærprogrammering, inkludert heltallsutvidelsen av dette, gjerne kalt «mixed-integer (linear) programming». Det finnes pakker for dette til de fleste programmeringsspråk, der man kan bruke ulike back-ends/«solvers», inkludert kommersielle (svært gode) som f.eks. Gurobi (https://www.gurobi.com/), som man lett kan få akademisk lisens på (men sjekk om lisensen dekker den typen bruk du ser for deg). Men det finnes også mange svært gode (om enn ikke like gode) open-source-solvere.

Om du bruker Python, er vel Pyomo (http://www.pyomo.org/) kanskje en grei front-end. PuLP (https://github.com/coin-or/pulp) er et annet alternativ.

Selv bruker jeg Julia (https://julialang.org/) til sånt som dette, og da pakken JuMP (https://jump.dev/). En myk start der finner du f.eks. i tutorial-delen av dokumentasjonen:

https://jump.dev/JuMP.jl/stable/tutorials/linear/introduction/

Det er ikke garantert at du kan få kodet inn alt du ønsker i et mixed-integer-program (MIP), men det er gode sjanser for at det er mulig. Det er også mulig å få til ulike former for rettferdighet, f.eks., som ikke nødvendigvis ser lineært ut ved første øyekast. (Jeg har implementert en del slikt i https://github.com/mlhetland/Allocations.jl, f.eks.) 

En del triks for å få kodet inn ting:

https://folk.idi.ntnu.no/mlh/algkon/lp_tricks.pdf

https://folk.idi.ntnu.no/mlh/algkon/ip_tricks.pdf

Om du heller vil (eller finner ut at du må) bruke et lokalt søk, så vet jeg ikke nødvendigvis hva som er best/cutting edge der, men å bare kjøre på med en helt enkel simulated annealing vil ofte kunne fungere rimelig bra, og vil jo være et enkelt sted å begynne.

Det finnes vel også pakker med ulike former for lokalt søk som «back-ends», så du kan prøve ulike varianter, selv om du selv kun trenger å implementere en fitness-funksjon og en mutasjonsoperator, f.eks. Jeg har ikke noen anbefalinger i hodet der, for øyeblikket, men det bør være mulig å finne, skulle jeg tro.

Mvh,

Magnus Lie Hetland
