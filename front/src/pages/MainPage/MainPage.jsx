import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import CoinCard from "@/components/CoinCard/CoinCard.jsx";
import CoinStatus from "@/components/CoinStatus/CoinStatus.jsx";

const MainPage = () => {
    return(
        <TemplatePage>
            <section>
                <CoinCard/>
                <CoinStatus/>
            </section>
        </TemplatePage>
    )
}

export default MainPage