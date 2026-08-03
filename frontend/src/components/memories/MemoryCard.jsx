import "./MemoryCard.css";

import { useState } from "react";
import { motion } from "framer-motion";
import toast from "react-hot-toast";

import {
  Heart,
  Clock3,
  Globe,
  ExternalLink,
  Eye,
  Trash2,
  Copy,
  Share2,
} from "lucide-react";

import MemoryDrawer from "./MemoryDrawer";

import {
  favoriteMemory,
  deleteMemory,
} from "../../services/memoryService";

const MemoryCard = ({ memory, onDelete }) => {

  const [favorite, setFavorite] = useState(
    memory.is_favorite || false
  );

  const [open, setOpen] = useState(false);

  const handleFavorite = async (e) => {

    e.stopPropagation();

    try {

      await favoriteMemory(memory.id);

      setFavorite((prev) => !prev);

      toast.success(
        favorite
          ? "Removed from favorites"
          : "Added to favorites"
      );

    } catch (err) {

      console.error(err);

      toast.error("Failed to update favorite");

    }

  };

  const handleDelete = async (e) => {

    e.stopPropagation();

    console.log("Memory object:", memory);
    console.log("Deleting ID:", memory.id);

    const ok = window.confirm("Delete this memory?");

    if (!ok) return;

    try {

      await deleteMemory(memory.id);

      toast.success("Memory deleted");

      if (onDelete) {
        onDelete(memory.id);
      }

    } catch (err) {

      console.error(err);

      toast.error("Delete failed");

    }

  };

  const handleCopy = async (e) => {

    e.stopPropagation();

    try {

      await navigator.clipboard.writeText(

        memory.url ||

        memory.raw_content ||

        memory.ai_summary ||

        ""

      );

      toast.success("Copied successfully");

    } catch {

      toast.error("Copy failed");

    }

  };

  const handleShare = async (e) => {

    e.stopPropagation();

    try {

      if (navigator.share) {

        await navigator.share({

          title: memory.title,

          text: memory.ai_summary,

          url: memory.url,

        });

      } else {

        await navigator.clipboard.writeText(

          memory.url || ""

        );

        toast.success("Link copied");

      }

    } catch (err) {

      console.log(err);

    }

  };

  return (

    <>

      <motion.div

        className="memory-card"

        whileHover={{

          y: -8,

          scale: 1.02,

        }}

      >

        <div className="memory-top">

          <div className="memory-info">

            <img

              className="memory-favicon"

              src={

                memory.favicon ||

                "https://www.google.com/s2/favicons?domain=" +

                memory.domain

              }

              alt="favicon"

            />

            <div>

              <h3>

                {memory.title}

              </h3>

              <span>

                {memory.domain}

              </span>

            </div>

          </div>

          <button

            className="icon-btn"

            onClick={handleFavorite}

          >

            <Heart

              size={18}

              color="#EF4444"

              fill={favorite ? "#EF4444" : "none"}

            />

          </button>

        </div>

        <p className="memory-summary">

          {

            memory.ai_summary ||

            "No AI summary available."

          }

        </p>

        <div className="memory-bottom">

          <div className="memory-meta">

            <span>

              <Clock3 size={15} />

              {memory.reading_time || 0} min

            </span>

            <span>

              <Eye size={15} />

              {memory.visit_count || 0}

            </span>

            <span>

              <Globe size={15} />

              {memory.domain}

            </span>

          </div>

          {

            memory.url && (

              <a

                href={memory.url}

                target="_blank"

                rel="noreferrer"

                className="visit-btn"

                onClick={(e) =>

                  e.stopPropagation()

                }

              >

                <ExternalLink size={18} />

              </a>

            )

          }

        </div>

        <div className="memory-actions">

          <button

            className="action-btn"

            onClick={() => setOpen(true)}

          >

            <Eye size={18} />

          </button>

          <button

            className="action-btn"

            onClick={handleCopy}

          >

            <Copy size={18} />

          </button>

          <button

            className="action-btn"

            onClick={handleShare}

          >

            <Share2 size={18} />

          </button>

          <button

            className="action-btn delete"

            onClick={handleDelete}

          >

            <Trash2 size={18} />

          </button>

        </div>

      </motion.div>

      <MemoryDrawer

        open={open}

        memory={memory}

        onClose={() => setOpen(false)}

      />

    </>

  );

};

export default MemoryCard;