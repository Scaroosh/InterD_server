import React, { useState } from 'react';
import axios from 'axios';
import classes from './ChatBotActionButtons.module.css';

const ChatBotActionButtons = () => {
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);
    const [formData, setFormData] = useState({
        cryptocurrency: '',
        tradeAmount: '',
        tradingStrategy: ''
    });
    const [botId, setBotId] = useState(null); // State to store bot_id

    const handleError = (err) => {
        if (err.response) {
            setError(`Error: ${err.response.status} ${err.response.statusText} - ${err.response.data}`);
        } else if (err.request) {
            setError('Error: No response received from server');
        } else {
            setError(`Error: ${err.message}`);
        }
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/create_bot", {
                owner_id: "6684b8c13a116176f4064ddd",
                ticker: formData.cryptocurrency,
                usdt_amount: formData.tradeAmount
            });
            const botData = res.data;
            if (botData && botData.bot_id) {
                setBotId(botData.bot_id); // Save bot_id in state
                setResponse("Bot created successfully");
            } else {
                setError("Failed to create bot");
            }
        } catch (err) {
            handleError(err);
        }
    };

    const startBot = async () => {
        if (!botId) {
            setError("Bot is not created yet");
            return;
        }

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/start_bot", {
                bot_id: botId
            });
            setResponse(res.data);
        } catch (err) {
            handleError(err);
        }
    };

    const stopBot = async () => {
        if (!botId) {
            setError("Bot is not created yet");
            return;
        }

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/stop_bot", {
                bot_id: botId,
                ticker: formData.cryptocurrency
            });
            setResponse(res.data);
        } catch (err) {
            handleError(err);
        }
    };

    const pauseBot = async () => {
        if (!botId) {
            setError("Bot is not created yet");
            return;
        }

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/pause_bot", {
                bot_id: botId,
                ticker: formData.cryptocurrency
            });
            setResponse(res.data);
        } catch (err) {
            handleError(err);
        }
    };

    const resumeBot = async () => {
        if (!botId) {
            setError("Bot is not created yet");
            return;
        }

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/resume_bot", {
                bot_id: botId,
                ticker: formData.cryptocurrency
            });
            setResponse(res.data);
        } catch (err) {
            handleError(err);
        }
    };

    const deleteBot = async () => {
        if (!botId) {
            setError("Bot is not created yet");
            return;
        }

        try {
            const res = await axios.post("http://127.0.0.1:8080/bot/delete_bot", {
                bot_id: botId,
            });
            setResponse(res.data);
        } catch (err) {
            handleError(err);
        }
    };

    return (
        <div>
            <form className={classes.form} onSubmit={handleSubmit}>
                <div>
                    <label>Cryptocurrency:</label>
                    <input
                        type="text"
                        name="cryptocurrency"
                        value={formData.cryptocurrency}
                        onChange={handleInputChange}
                    />
                </div>
                <div>
                    <label>Trade Amount:</label>
                    <input
                        type="number"
                        name="tradeAmount"
                        value={formData.tradeAmount}
                        onChange={handleInputChange}
                    />
                </div>
                <div>
                    <label>Trading Strategy:</label>
                    <select
                        name="tradingStrategy"
                        value={formData.tradingStrategy}
                        onChange={handleInputChange}
                    >
                        <option value="">Select strategy...</option>
                        <option value="strategy1">Strategy 1</option>
                        <option value="strategy2">Strategy 2</option>
                    </select>
                </div>
                <button type="submit">Submit</button>
            </form>
            <div className={classes.container}>
                <button className={classes.buttons} onClick={startBot}>start</button>
                <button className={classes.buttons} onClick={stopBot}>stop</button>
                <button className={classes.buttons} onClick={pauseBot}>pause</button>
                <button className={classes.buttons} onClick={resumeBot}>resume</button>
                <button className={classes.buttons} onClick={deleteBot}>delete</button>
            </div>
            {response && (
                <div className={classes.response}>
                    <div>Response: {JSON.stringify(response)}</div>
                </div>
            )}
            {error && <div className={classes.error}>Error: {error}</div>}
        </div>
    );
};

export default ChatBotActionButtons;