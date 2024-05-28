import Footer from "@/components/Footer/Footer.jsx";
import Header from "@/components/Header/Header.jsx";
import classes from "./TemplatePage.module.css"
// eslint-disable-next-line react/prop-types
function TemplatePage({children}) {
    return (
        <section className={classes.container}>
            <Header />
            <main className={classes.main}>
                {children}
            </main>
            <Footer />
        </section>
    )
}

export default TemplatePage