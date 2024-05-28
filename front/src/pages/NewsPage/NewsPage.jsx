import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import classes from "./NewsPage.module.css"
import newsPageImg from "@/assets/news_page_img.png"
const NewsPage = () => {
    return(
        <TemplatePage>
            <section className={classes.container}>
                <div>
                    <p className={classes.title}>We make the news.</p>
                    <ul className={classes.article_info}>
                        <li className={classes.article_date}>21 May</li>
                        <li><p className={classes.article_text}>How much interest does your bank pay? - Trading Bot launches a broad interest campaign on TV, radio and billboard advertising in Germany's largest cities</p></li>
                        <li className={classes.article_date}>28 May</li>
                        <li><p className={classes.article_text}>Berlin based tights label saint sass and Trading Bot join forces on International Women's Day to raise awareness for the importance of female retirement savings.</p></li>
                        <li className={classes.article_date}>04 June</li>
                        <li><p className={classes.article_text}>Trading Bot celebrates its 5th birthday with 4 million customers and introduces a new card with a 1 percent Saveback reward for every card payment.</p></li>
                    </ul>
                </div>
                <div className={classes.contact_info}>
                    <img src={newsPageImg} alt="newsPageImg"/>
                    <div className={classes.contact_text_container}>
                            <p className={classes.contact}>Contacts</p>
                            <p className={classes.contact_text}>24/7 Customer Support Trading bot is there for you every step of the way. We offer 24/7 support, allowing our clients to contact with any of our friendly and experienced customer service agents throughout the trading week. Whether you have questions or you would just like to provide us with feedback regarding our services, we’re here for you.</p>
                    </div>
                </div>
            </section>
        </TemplatePage>
    )
}

export default NewsPage