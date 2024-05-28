import classes from "./SearchBar.module.css"
const SearchBar = () => {
    return(
        <>

            <div className={classes.search_container}>
                <input type="text" className={classes.search_input} placeholder="Search..."/>
                <button className={classes.search_button}>
                    <i className="fa fa-search"></i> {/* Иконка Font Awesome */}
                </button>
            </div>
        </>
    )
}

export default SearchBar